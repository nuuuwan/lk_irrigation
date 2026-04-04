# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_21:10:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,260 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 21:10:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.021 |  |
| 2026-04-04 21:09:19 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-04-04 21:09:07 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.027 |  |
| 2026-04-04 21:07:57 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | -0.010 |  |
| 2026-04-04 21:06:34 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:05:59 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:05:13 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.120 |  |
| 2026-04-04 21:04:44 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-04-04 21:04:12 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:04:06 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | -0.041 |  |
| 2026-04-04 21:03:59 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.013 |  |
| 2026-04-04 21:03:52 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:03:47 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:03:46 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-04 21:03:43 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:03:37 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:03:31 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-04-04 21:03:22 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-04 21:03:11 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.023 |  |
| 2026-04-04 21:03:00 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-04 21:02:59 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-04 21:02:52 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:02:31 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-04-04 21:02:27 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:02:26 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-04-04 21:02:20 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-04 21:02:18 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.186 |  |
| 2026-04-04 21:02:11 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.650 | 🔺 Rising |
| 2026-04-04 21:02:11 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-04-04 21:02:10 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 21:02:06 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 21:02:03 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:02:00 | Manampitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-04 21:01:54 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:01:44 | Siyambalanduwa (Heda Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:01:34 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:00:29 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 20:17:52 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 21:02:11 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.650 | 🔺 Rising |
| 2026-04-04 21:02:31 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-04-04 21:03:00 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-04 21:03:46 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-04 21:02:00 | Manampitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-04 21:02:06 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 21:03:22 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-04 21:02:10 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 21:00:29 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:02:03 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:04:12 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:01:34 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:58:33 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:05:59 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:03:43 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:02:52 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:03:47 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:02:27 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:01:44 | Siyambalanduwa (Heda Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:03:37 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:06:34 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:03:52 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:03:31 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-04-04 21:09:19 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-04-04 21:02:20 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-04 21:02:26 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-04-04 21:07:57 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | -0.010 |  |
| 2026-04-04 21:02:59 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-04 21:04:44 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-04-04 21:03:59 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.013 |  |
| 2026-04-04 21:10:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.021 |  |
| 2026-04-04 21:03:11 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.023 |  |
| 2026-04-04 21:09:07 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.027 |  |
| 2026-04-04 21:02:11 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-04-04 18:01:01 | Thanthirimale (Malwathu Oya) | 2.52 | 🟢 Normal | -0.031 |  |
| 2026-04-04 21:04:06 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | -0.041 |  |
| 2026-04-04 18:01:27 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.050 |  |
| 2026-04-04 21:05:13 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.120 |  |
| 2026-04-04 21:02:18 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.186 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)