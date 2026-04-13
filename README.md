# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_12:13:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,920 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 12:13:11 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | -0.008 |  |
| 2026-04-13 12:13:05 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:12:38 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:09:34 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:09:24 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-13 12:08:53 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-04-13 12:08:27 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-13 12:08:07 | Ellagawa (Kalu Ganga) | 5.78 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-13 12:07:32 | Magura (Kalu Ganga) | 3.01 | 🟢 Normal | -0.177 |  |
| 2026-04-13 12:07:22 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-04-13 12:05:04 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | -0.072 |  |
| 2026-04-13 12:04:33 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-04-13 12:04:33 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:04:11 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-04-13 12:04:10 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:04:00 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.076 |  |
| 2026-04-13 12:03:57 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-13 12:03:24 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.178 |  |
| 2026-04-13 12:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.52 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:03:23 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-04-13 12:02:57 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:02:50 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:02:50 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.049 |  |
| 2026-04-13 12:02:39 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-04-13 12:02:34 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:02:33 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-13 12:02:32 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.022 |  |
| 2026-04-13 12:02:19 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-04-13 12:02:19 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.024 |  |
| 2026-04-13 12:02:14 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.090 |  |
| 2026-04-13 12:02:05 | Katharagama (Menik Ganga) | -0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:02:03 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | -0.024 |  |
| 2026-04-13 12:01:53 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-13 12:01:34 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:01:32 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:01:32 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.030 |  |
| 2026-04-13 12:01:25 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:00:52 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-04-13 12:00:20 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 12:02:39 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-04-13 12:08:53 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-04-13 12:07:22 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-04-13 12:09:24 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-13 12:03:57 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-13 12:02:33 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-13 12:08:27 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-13 12:08:07 | Ellagawa (Kalu Ganga) | 5.78 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-13 12:01:25 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:13:05 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:01:34 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:12:38 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:04:10 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:01:32 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:02:57 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:02:34 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:02:05 | Katharagama (Menik Ganga) | -0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:04:33 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:02:50 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:09:34 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.52 | 🟢 Normal | 0.000 |  |
| 2026-04-13 12:13:11 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | -0.008 |  |
| 2026-04-13 12:04:33 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-04-13 12:00:52 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-04-13 12:01:53 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-13 11:03:07 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.019 |  |
| 2026-04-13 12:04:11 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-04-13 12:00:20 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-04-13 12:03:23 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-04-13 12:02:32 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.022 |  |
| 2026-04-13 12:02:03 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | -0.024 |  |
| 2026-04-13 12:02:19 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.024 |  |
| 2026-04-13 12:01:32 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.030 |  |
| 2026-04-13 12:02:50 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.049 |  |
| 2026-04-13 12:05:04 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | -0.072 |  |
| 2026-04-13 12:04:00 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.076 |  |
| 2026-04-13 12:02:14 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.090 |  |
| 2026-04-13 12:07:32 | Magura (Kalu Ganga) | 3.01 | 🟢 Normal | -0.177 |  |
| 2026-04-13 12:03:24 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.178 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)