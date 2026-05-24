# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_20:12:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **160,640 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 20:12:26 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -0.044 |  |
| 2026-05-24 20:11:19 | Rathnapura (Kalu Ganga) | 4.85 | 🟢 Normal | 0.402 | 🔺 Rising |
| 2026-05-24 20:09:49 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-24 20:08:40 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-05-24 20:08:24 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:07:54 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:06:33 | Kithulgala (Kelani Ganga) | 2.21 | 🟢 Normal | -0.020 |  |
| 2026-05-24 20:06:20 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.009 |  |
| 2026-05-24 20:06:00 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:05:57 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-05-24 20:05:43 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | -0.034 |  |
| 2026-05-24 20:05:05 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-24 20:04:53 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:04:15 | Ellagawa (Kalu Ganga) | 9.55 | 🟢 Normal | -0.039 |  |
| 2026-05-24 20:04:08 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | -0.060 |  |
| 2026-05-24 20:04:02 | Putupaula (Kalu Ganga) | 3.27 | 🟡 Alert | 0.000 |  |
| 2026-05-24 20:04:00 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-24 20:04:00 | Deraniyagala (Kelani Ganga) | 3.68 | 🟢 Normal | -0.283 |  |
| 2026-05-24 20:02:50 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 20:02:47 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-05-24 20:02:45 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-24 20:02:25 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:02:24 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.18 | 🟡 Alert | -0.020 |  |
| 2026-05-24 20:02:17 | Dunamale (Aththanagalu Oya) | 2.88 | 🟢 Normal | -0.080 |  |
| 2026-05-24 20:02:01 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.015 |  |
| 2026-05-24 20:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.449 | 🔺 Rising |
| 2026-05-24 20:01:54 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:01:30 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:01:28 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:01:25 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:01:20 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:01:10 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:00:22 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:00:13 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 20:04:02 | Putupaula (Kalu Ganga) | 3.27 | 🟡 Alert | 0.000 |  |
| 2026-05-24 20:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.18 | 🟡 Alert | -0.020 |  |
| 2026-05-24 20:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.449 | 🔺 Rising |
| 2026-05-24 20:11:19 | Rathnapura (Kalu Ganga) | 4.85 | 🟢 Normal | 0.402 | 🔺 Rising |
| 2026-05-24 20:09:49 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-24 20:04:00 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-24 20:05:05 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-24 20:02:50 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 18:00:57 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:00:13 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:02:24 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:01:28 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:01:54 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:01:30 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:50 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:04:53 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:06:00 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:00:22 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:01:20 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:08:24 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:01:25 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:42 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:07:54 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-24 19:05:19 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:01:10 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:02:25 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 20:06:20 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.009 |  |
| 2026-05-24 20:08:40 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-05-24 20:02:45 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-24 20:02:01 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.015 |  |
| 2026-05-24 20:05:57 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-05-24 20:02:47 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-05-24 20:06:33 | Kithulgala (Kelani Ganga) | 2.21 | 🟢 Normal | -0.020 |  |
| 2026-05-24 20:05:43 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | -0.034 |  |
| 2026-05-24 20:04:15 | Ellagawa (Kalu Ganga) | 9.55 | 🟢 Normal | -0.039 |  |
| 2026-05-24 20:12:26 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -0.044 |  |
| 2026-05-24 20:04:08 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | -0.060 |  |
| 2026-05-24 20:02:17 | Dunamale (Aththanagalu Oya) | 2.88 | 🟢 Normal | -0.080 |  |
| 2026-05-24 20:04:00 | Deraniyagala (Kelani Ganga) | 3.68 | 🟢 Normal | -0.283 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)