# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_13:07:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,305 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 13:07:15 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.019 |  |
| 2026-05-07 13:07:13 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-07 13:06:23 | Galgamuwa (Mee Oya) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-05-07 13:06:22 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-07 13:06:19 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-07 13:06:02 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-07 13:05:41 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.031 |  |
| 2026-05-07 13:05:33 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-07 13:05:28 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-07 13:05:05 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.049 |  |
| 2026-05-07 13:04:51 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-07 13:04:40 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-05-07 13:04:13 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-07 13:04:06 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.062 |  |
| 2026-05-07 13:03:48 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-07 13:03:35 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | -0.162 |  |
| 2026-05-07 13:03:30 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 13:03:27 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-07 13:03:11 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.109 |  |
| 2026-05-07 13:03:05 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-05-07 13:02:58 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-07 13:02:51 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.052 |  |
| 2026-05-07 13:02:46 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-07 13:02:36 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 13:02:35 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-07 13:02:31 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-07 13:02:29 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-05-07 13:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 13:02:10 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-07 13:01:57 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-07 13:01:38 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-05-07 13:01:06 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | -0.064 |  |
| 2026-05-07 13:00:33 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-05-07 13:00:32 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-07 13:00:16 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 13:03:48 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-07 13:02:31 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-07 13:06:02 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-07 13:06:22 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-07 13:05:33 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-07 12:06:38 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-07 13:05:28 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-07 13:06:19 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-07 13:04:13 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-07 13:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 13:03:30 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 13:02:58 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-07 13:01:57 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-07 12:01:12 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-07 13:02:36 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 13:03:27 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-07 13:04:51 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-07 13:07:13 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-07 13:02:10 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-07 13:02:29 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-05-07 13:03:05 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-05-07 13:02:46 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-07 13:00:33 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-05-07 13:02:35 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-07 13:04:40 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-05-07 13:01:38 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-05-07 13:07:15 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.019 |  |
| 2026-05-07 13:06:23 | Galgamuwa (Mee Oya) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-05-07 13:00:16 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.021 |  |
| 2026-05-07 13:05:41 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.031 |  |
| 2026-05-07 12:03:15 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.040 |  |
| 2026-05-07 13:05:05 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.049 |  |
| 2026-05-07 13:02:51 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.052 |  |
| 2026-05-07 13:04:06 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.062 |  |
| 2026-05-07 13:01:06 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | -0.064 |  |
| 2026-05-07 12:06:13 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | -0.072 |  |
| 2026-05-07 12:00:51 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.087 |  |
| 2026-05-07 13:03:11 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.109 |  |
| 2026-05-07 13:03:35 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | -0.162 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)