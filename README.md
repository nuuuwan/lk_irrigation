# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_10:23:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,983 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 10:23:29 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:18:58 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:14:11 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-07 10:13:33 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:11:22 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:08:58 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.010 |  |
| 2026-01-07 10:08:00 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.019 |  |
| 2026-01-07 10:07:57 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:07:37 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.087 |  |
| 2026-01-07 10:07:31 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.082 |  |
| 2026-01-07 10:07:08 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.009 |  |
| 2026-01-07 10:06:34 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.015 |  |
| 2026-01-07 10:05:39 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:05:16 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-01-07 10:04:54 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-07 10:04:30 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:04:11 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.050 |  |
| 2026-01-07 10:04:08 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:03:45 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 10:03:34 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:03:33 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 10:03:25 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:03:02 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:03:00 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-01-07 10:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | -0.040 |  |
| 2026-01-07 10:02:22 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.140 |  |
| 2026-01-07 10:02:08 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.060 |  |
| 2026-01-07 10:02:08 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-01-07 10:01:58 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-07 10:01:42 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:01:35 | Weraganthota (Mahaweli Ganga) | -1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-07 10:01:30 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:01:28 | Manampitiya (Mahaweli Ganga) | 2.87 | 🟢 Normal | -0.099 |  |
| 2026-01-07 10:01:24 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-01-07 10:01:16 | Horowpothana (Yan Oya) | 2.76 | 🟢 Normal | -0.061 |  |
| 2026-01-07 10:01:13 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:01:10 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:00:49 | Siyambalanduwa (Heda Oya) | 1.82 | 🟢 Normal | -0.040 |  |
| 2026-01-07 10:00:38 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 10:03:45 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 10:03:33 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 10:14:11 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-07 10:01:10 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:01:13 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:01:30 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-07 09:04:57 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:13:33 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:18:58 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:11:22 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:03:02 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:05:39 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:04:08 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:01:42 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:07:57 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:04:30 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:03:25 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:23:29 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-07 10:07:08 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.009 |  |
| 2026-01-07 10:04:54 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-07 10:08:58 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.010 |  |
| 2026-01-07 10:01:58 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-07 10:05:16 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-01-07 10:01:35 | Weraganthota (Mahaweli Ganga) | -1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-07 10:01:24 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-01-07 10:03:00 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-01-07 10:02:08 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-01-07 10:06:34 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.015 |  |
| 2026-01-07 10:08:00 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.019 |  |
| 2026-01-07 10:00:38 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-01-07 10:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | -0.040 |  |
| 2026-01-07 10:00:49 | Siyambalanduwa (Heda Oya) | 1.82 | 🟢 Normal | -0.040 |  |
| 2026-01-07 10:04:11 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.050 |  |
| 2026-01-07 10:02:08 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.060 |  |
| 2026-01-07 10:01:16 | Horowpothana (Yan Oya) | 2.76 | 🟢 Normal | -0.061 |  |
| 2026-01-07 10:07:31 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.082 |  |
| 2026-01-07 10:07:37 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.087 |  |
| 2026-01-07 10:01:28 | Manampitiya (Mahaweli Ganga) | 2.87 | 🟢 Normal | -0.099 |  |
| 2026-01-07 10:02:22 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)