# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_12:09:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,958 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 12:09:18 | Panadugama (Nilwala Ganga) | 3.64 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:09:13 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-01-08 12:09:01 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:08:42 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:07:14 | Padiyathalawa (Maduru Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:06:15 | Panadugama (Nilwala Ganga) | 3.64 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:06:05 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-08 12:05:41 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:05:35 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-08 12:05:31 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.043 |  |
| 2026-01-08 12:05:09 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.048 |  |
| 2026-01-08 12:04:37 | Katharagama (Menik Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:04:22 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.141 |  |
| 2026-01-08 12:03:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-08 12:03:33 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:03:18 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:03:17 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:03:14 | Siyambalanduwa (Heda Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:03:12 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.010 |  |
| 2026-01-08 12:03:05 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:03:05 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-01-08 12:02:52 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:02:24 | Weraganthota (Mahaweli Ganga) | -1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:02:16 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.021 |  |
| 2026-01-08 12:02:15 | Manampitiya (Mahaweli Ganga) | 2.44 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-08 12:02:13 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.040 |  |
| 2026-01-08 12:02:13 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-08 12:02:10 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:01:48 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-01-08 12:01:32 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:01:30 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-08 12:01:29 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 12:01:29 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:01:22 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:00:26 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.034 |  |
| 2026-01-08 12:00:16 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:59:46 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:58:59 | Horowpothana (Yan Oya) | 2.29 | 🟢 Normal | -0.019 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 12:02:15 | Manampitiya (Mahaweli Ganga) | 2.44 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-08 12:01:30 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-08 12:03:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-08 12:02:13 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-08 12:05:35 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-08 12:01:29 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 12:02:24 | Weraganthota (Mahaweli Ganga) | -1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:01:32 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:00:16 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:01:22 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:01:29 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:03:33 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:23:05 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:03:18 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:09:18 | Panadugama (Nilwala Ganga) | 3.64 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:07:14 | Padiyathalawa (Maduru Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:03:17 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:02:52 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:03:14 | Siyambalanduwa (Heda Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:09:01 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:04:37 | Katharagama (Menik Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:05:41 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:08:42 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:03:05 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-08 12:02:10 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-08 11:22:48 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-01-08 12:03:12 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.010 |  |
| 2026-01-08 12:03:05 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-01-08 12:06:05 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-08 12:01:48 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-01-08 11:58:59 | Horowpothana (Yan Oya) | 2.29 | 🟢 Normal | -0.019 |  |
| 2026-01-08 12:09:13 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-01-08 12:02:16 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.021 |  |
| 2026-01-08 12:00:26 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.034 |  |
| 2026-01-08 12:02:13 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.040 |  |
| 2026-01-08 12:05:31 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.043 |  |
| 2026-01-08 12:05:09 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.048 |  |
| 2026-01-08 12:04:22 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.141 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)