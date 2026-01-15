# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--15_16:12:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **46,380 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 16:12:30 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-01-15 16:11:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-01-15 16:11:44 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.009 |  |
| 2026-01-15 16:10:21 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.043 |  |
| 2026-01-15 16:09:38 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.035 |  |
| 2026-01-15 16:09:19 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.038 |  |
| 2026-01-15 16:08:51 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:07:23 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-15 16:07:14 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.047 |  |
| 2026-01-15 16:07:08 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:07:05 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.038 |  |
| 2026-01-15 16:06:59 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.057 |  |
| 2026-01-15 16:06:35 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.028 |  |
| 2026-01-15 16:06:15 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:05:09 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-01-15 16:05:05 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:04:37 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-01-15 16:04:03 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:03:55 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:03:23 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:03:03 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-01-15 16:03:01 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-01-15 16:02:51 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:02:26 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:02:08 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 16:01:50 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-15 16:01:48 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-15 16:01:45 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-15 16:01:41 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:01:38 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-15 16:01:34 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-15 16:01:31 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:01:29 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | -0.110 |  |
| 2026-01-15 16:01:29 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-15 16:01:02 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:00:51 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:00:41 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 15:01:15 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-01-15 16:01:48 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-15 16:02:08 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 16:01:31 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:01:41 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:02:51 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:04:03 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:07:08 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:03:23 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:02:26 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:01:02 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:03:55 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:06:15 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:00:51 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:05:05 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:08:51 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:00:41 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:05:57 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:12:30 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-01-15 16:11:44 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.009 |  |
| 2026-01-15 16:03:03 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-01-15 16:01:38 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-15 16:01:29 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-15 16:01:34 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-15 16:05:09 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-01-15 16:01:45 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-15 16:07:23 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-15 16:01:50 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-15 16:04:37 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-01-15 16:11:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-01-15 16:03:01 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-01-15 16:06:35 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.028 |  |
| 2026-01-15 16:09:38 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.035 |  |
| 2026-01-15 16:09:19 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.038 |  |
| 2026-01-15 16:07:05 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.038 |  |
| 2026-01-15 16:10:21 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.043 |  |
| 2026-01-15 16:07:14 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.047 |  |
| 2026-01-15 16:06:59 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.057 |  |
| 2026-01-15 16:01:29 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)