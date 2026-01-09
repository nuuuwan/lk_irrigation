# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--09_18:10:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **41,108 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 18:10:16 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 18:09:12 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-01-09 18:08:55 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-01-09 18:08:11 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-09 18:08:00 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-01-09 18:07:35 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:06:53 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:06:49 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:06:47 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-01-09 18:06:00 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:05:37 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:05:26 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:04:44 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:04:16 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-09 18:04:06 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:03:57 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 18:03:45 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-01-09 18:03:36 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:03:16 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 18:03:09 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:03:02 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-09 18:02:47 | Manampitiya (Mahaweli Ganga) | 2.42 | 🟢 Normal | -0.077 |  |
| 2026-01-09 18:02:41 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:02:31 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.021 |  |
| 2026-01-09 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:02:07 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:02:06 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 18:02:00 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:01:35 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:01:33 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:01:32 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | -0.130 |  |
| 2026-01-09 18:01:29 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 18:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:01:05 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:00:55 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:00:39 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:00:08 | Weraganthota (Mahaweli Ganga) | -1.21 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 18:06:47 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-01-09 18:03:45 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-01-09 18:04:16 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-09 18:03:02 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-09 18:01:29 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 18:03:57 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 17:13:03 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 18:10:16 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 18:03:16 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 18:02:06 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 18:08:11 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-09 18:02:00 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:04:06 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:03:36 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:02:07 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:06:49 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:11:39 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:05:37 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:00:55 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:00:39 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:04:44 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:05:26 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:07:35 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:03:09 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:01:33 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 18:09:12 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-01-09 18:08:55 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-01-09 18:06:53 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:02:41 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:01:35 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:01:05 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:06:00 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:00:08 | Weraganthota (Mahaweli Ganga) | -1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:08:00 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-01-09 18:02:31 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.021 |  |
| 2026-01-09 18:02:47 | Manampitiya (Mahaweli Ganga) | 2.42 | 🟢 Normal | -0.077 |  |
| 2026-01-09 18:01:32 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | -0.130 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)