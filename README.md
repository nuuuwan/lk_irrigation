# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_09:16:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **221,046 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 09:16:11 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:12:31 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-31 09:12:21 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-31 09:11:33 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-31 09:09:29 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-31 09:09:10 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:07:20 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:06:49 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:06:35 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:06:31 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.030 |  |
| 2026-07-31 09:06:04 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:05:45 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:05:28 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-07-31 09:05:24 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:05:15 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:04:45 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-07-31 09:04:34 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:04:22 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:03:49 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:03:47 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-07-31 09:03:40 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:03:33 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-07-31 09:03:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.059 |  |
| 2026-07-31 09:03:15 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.113 |  |
| 2026-07-31 09:03:01 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:02:57 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-07-31 09:02:51 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.040 |  |
| 2026-07-31 09:02:48 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 09:02:44 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | -0.030 |  |
| 2026-07-31 09:02:33 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-07-31 09:02:24 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:02:22 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:02:09 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:01:42 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:01:24 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-07-31 09:01:22 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 09:01:20 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.058 |  |
| 2026-07-31 09:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:00:25 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:00:12 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 09:03:47 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-07-31 09:04:45 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-07-31 09:01:22 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 09:09:29 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-31 09:12:21 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-31 09:11:33 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-31 09:02:48 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 08:02:47 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 09:12:31 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-31 09:05:15 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:00:12 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:03:49 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:05:45 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:06:49 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:04:34 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:16:11 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:06:35 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:06:04 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:02:24 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:02:09 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:03:01 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:09:10 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:02:22 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:01:42 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:03:40 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:00:25 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:04:22 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 09:03:33 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-07-31 09:02:33 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-07-31 09:02:57 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-07-31 09:01:24 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-07-31 09:02:44 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | -0.030 |  |
| 2026-07-31 09:06:31 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.030 |  |
| 2026-07-31 09:05:28 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-07-31 09:02:51 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.040 |  |
| 2026-07-31 09:01:20 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.058 |  |
| 2026-07-31 09:03:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.059 |  |
| 2026-07-31 09:03:15 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)