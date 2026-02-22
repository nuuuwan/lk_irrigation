# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_16:18:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,120 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 16:18:55 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-02-22 16:16:39 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.049 |  |
| 2026-02-22 16:11:05 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.234 |  |
| 2026-02-22 16:08:36 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 16:07:41 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.083 |  |
| 2026-02-22 16:07:22 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-02-22 16:07:22 | Rathnapura (Kalu Ganga) | 3.06 | 🟢 Normal | -0.181 |  |
| 2026-02-22 16:07:14 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.057 |  |
| 2026-02-22 16:07:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | -0.020 |  |
| 2026-02-22 16:06:53 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-22 16:06:40 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-02-22 16:06:37 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 16:06:33 | Peradeniya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.028 |  |
| 2026-02-22 16:06:23 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-02-22 16:06:19 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.087 |  |
| 2026-02-22 16:05:30 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | -0.049 |  |
| 2026-02-22 16:05:13 | Glencourse (Kelani Ganga) | 9.68 | 🟢 Normal | -0.118 |  |
| 2026-02-22 16:04:51 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 16:04:48 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-22 16:04:02 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 16:03:47 | Ellagawa (Kalu Ganga) | 7.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-22 16:03:44 | Manampitiya (Mahaweli Ganga) | 3.86 | 🟡 Alert | -0.114 |  |
| 2026-02-22 16:03:17 | Hanwella (Kelani Ganga) | 2.09 | 🟢 Normal | -0.120 |  |
| 2026-02-22 16:03:01 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-22 16:03:00 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | -0.019 |  |
| 2026-02-22 16:02:33 | Thanamalwila (Kirindi Oya) | 1.51 | 🟢 Normal | -0.031 |  |
| 2026-02-22 16:02:28 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.069 |  |
| 2026-02-22 16:02:19 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.031 |  |
| 2026-02-22 16:02:09 | Putupaula (Kalu Ganga) | 1.56 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-22 16:02:05 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-02-22 16:02:01 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.031 |  |
| 2026-02-22 16:01:57 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-22 16:01:43 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.039 |  |
| 2026-02-22 16:01:42 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.030 |  |
| 2026-02-22 16:01:40 | Kithulgala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.111 |  |
| 2026-02-22 16:01:37 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.031 |  |
| 2026-02-22 16:01:28 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.030 |  |
| 2026-02-22 16:01:06 | Padiyathalawa (Maduru Oya) | 1.27 | 🟢 Normal | -0.030 |  |
| 2026-02-22 16:01:04 | Nakkala (Kumbukkan Oya) | 1.31 | 🟢 Normal | -0.039 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 16:07:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | -0.020 |  |
| 2026-02-22 16:03:44 | Manampitiya (Mahaweli Ganga) | 3.86 | 🟡 Alert | -0.114 |  |
| 2026-02-22 16:07:22 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-02-22 16:01:57 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-22 16:02:09 | Putupaula (Kalu Ganga) | 1.56 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-22 16:03:01 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-22 16:03:47 | Ellagawa (Kalu Ganga) | 7.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-22 16:08:36 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 16:04:51 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 16:18:55 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-02-22 16:04:02 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 16:04:48 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-22 16:06:37 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 16:06:23 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-02-22 16:06:53 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-22 16:06:40 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-02-22 16:03:00 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | -0.019 |  |
| 2026-02-22 16:02:05 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-02-22 16:06:33 | Peradeniya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.028 |  |
| 2026-02-22 16:01:06 | Padiyathalawa (Maduru Oya) | 1.27 | 🟢 Normal | -0.030 |  |
| 2026-02-22 16:01:28 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.030 |  |
| 2026-02-22 16:01:42 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.030 |  |
| 2026-02-22 16:02:01 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.031 |  |
| 2026-02-22 16:01:37 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.031 |  |
| 2026-02-22 16:02:19 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.031 |  |
| 2026-02-22 16:02:33 | Thanamalwila (Kirindi Oya) | 1.51 | 🟢 Normal | -0.031 |  |
| 2026-02-22 16:01:43 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.039 |  |
| 2026-02-22 16:01:04 | Nakkala (Kumbukkan Oya) | 1.31 | 🟢 Normal | -0.039 |  |
| 2026-02-22 16:16:39 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.049 |  |
| 2026-02-22 16:05:30 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | -0.049 |  |
| 2026-02-22 16:07:14 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.057 |  |
| 2026-02-22 16:02:28 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.069 |  |
| 2026-02-22 16:07:41 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.083 |  |
| 2026-02-22 16:06:19 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.087 |  |
| 2026-02-22 16:01:40 | Kithulgala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.111 |  |
| 2026-02-22 16:05:13 | Glencourse (Kelani Ganga) | 9.68 | 🟢 Normal | -0.118 |  |
| 2026-02-22 16:03:17 | Hanwella (Kelani Ganga) | 2.09 | 🟢 Normal | -0.120 |  |
| 2026-02-22 16:07:22 | Rathnapura (Kalu Ganga) | 3.06 | 🟢 Normal | -0.181 |  |
| 2026-02-22 16:11:05 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.234 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)