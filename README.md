# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--16_16:09:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **47,283 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 16:09:32 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-16 16:07:36 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.075 |  |
| 2026-01-16 16:07:34 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.047 |  |
| 2026-01-16 16:07:29 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:07:02 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:06:19 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:06:18 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:05:56 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 16:05:31 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:05:23 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-16 16:05:07 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:05:06 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-16 16:04:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.061 |  |
| 2026-01-16 16:04:41 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:04:29 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:04:19 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.050 |  |
| 2026-01-16 16:04:13 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 16:03:43 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | -0.011 |  |
| 2026-01-16 16:03:36 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | -0.029 |  |
| 2026-01-16 16:03:22 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:02:49 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:02:43 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:02:23 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-16 16:02:17 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.072 |  |
| 2026-01-16 16:02:14 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.89 | 🟢 Normal | -0.040 |  |
| 2026-01-16 16:02:10 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-01-16 16:02:05 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:01:55 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:01:53 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-16 16:01:53 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:01:43 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:01:28 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | -0.132 |  |
| 2026-01-16 16:01:09 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:00:40 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-16 16:00:18 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-01-16 16:00:16 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | -0.021 |  |
| 2026-01-16 15:23:41 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.008 |  |
| 2026-01-16 15:13:47 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 16:05:06 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-16 16:04:13 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 16:05:56 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 16:09:32 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-16 16:01:09 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:01:43 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:02:49 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:01:53 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:03:22 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:05:07 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:04:29 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:02:14 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:02:05 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:04:41 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:07:02 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:07:29 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:06:19 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-16 16:02:43 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:23:41 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.008 |  |
| 2026-01-16 15:06:43 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.009 |  |
| 2026-01-16 15:11:13 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.009 |  |
| 2026-01-16 16:05:23 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-16 16:02:23 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-16 16:02:10 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-01-16 16:00:40 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-16 16:00:18 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-01-16 16:01:53 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-16 15:03:27 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-16 16:03:43 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | -0.011 |  |
| 2026-01-16 15:01:27 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-01-16 16:00:16 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | -0.021 |  |
| 2026-01-16 16:03:36 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | -0.029 |  |
| 2026-01-16 16:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.89 | 🟢 Normal | -0.040 |  |
| 2026-01-16 16:07:34 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.047 |  |
| 2026-01-16 16:04:19 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.050 |  |
| 2026-01-16 16:04:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.061 |  |
| 2026-01-16 16:02:17 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.072 |  |
| 2026-01-16 16:07:36 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.075 |  |
| 2026-01-16 16:01:28 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)