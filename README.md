# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_09:13:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,490 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 09:13:03 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-16 09:10:38 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:10:34 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.072 |  |
| 2026-04-16 09:10:13 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | -0.018 |  |
| 2026-04-16 09:10:01 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-04-16 09:09:48 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:07:38 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-16 09:07:09 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-04-16 09:06:46 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.019 |  |
| 2026-04-16 09:06:17 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:06:01 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:04:56 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-04-16 09:04:29 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-04-16 09:03:56 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:03:54 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-16 09:03:45 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:03:42 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.031 |  |
| 2026-04-16 09:03:04 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.022 |  |
| 2026-04-16 09:03:01 | Hanwella (Kelani Ganga) | 0.89 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-16 09:02:57 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-04-16 09:02:51 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:02:50 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:02:48 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-04-16 09:02:48 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.050 |  |
| 2026-04-16 09:02:44 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:02:26 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.117 |  |
| 2026-04-16 09:02:24 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | -0.179 |  |
| 2026-04-16 09:02:23 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:02:15 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | -0.088 |  |
| 2026-04-16 09:02:12 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -0.029 |  |
| 2026-04-16 09:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.070 |  |
| 2026-04-16 09:02:05 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-16 09:01:53 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:01:44 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-04-16 09:01:36 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-16 09:01:24 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:00:21 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:00:16 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:00:14 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.100 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 09:02:48 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-04-16 09:03:01 | Hanwella (Kelani Ganga) | 0.89 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-16 09:07:38 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-16 09:13:03 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-16 09:00:16 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:06:01 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:01:24 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:02:51 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:02:50 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-16 08:03:37 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:03:45 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:09:48 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:06:17 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:02:23 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:03:56 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:02:44 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:01:53 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:10:38 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-04-16 09:03:54 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-16 09:02:05 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-16 09:07:09 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-04-16 09:04:56 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-04-16 09:01:36 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-16 09:10:01 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-04-16 09:10:13 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | -0.018 |  |
| 2026-04-16 09:06:46 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.019 |  |
| 2026-04-16 09:02:57 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-04-16 09:04:29 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-04-16 09:03:04 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.022 |  |
| 2026-04-16 09:02:12 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -0.029 |  |
| 2026-04-16 09:01:44 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-04-16 09:03:42 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.031 |  |
| 2026-04-16 09:02:48 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.050 |  |
| 2026-04-16 09:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.070 |  |
| 2026-04-16 09:10:34 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.072 |  |
| 2026-04-16 09:02:15 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | -0.088 |  |
| 2026-04-16 09:00:14 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.100 |  |
| 2026-04-16 09:02:26 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.117 |  |
| 2026-04-16 09:02:24 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | -0.179 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)