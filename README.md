# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_14:30:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **135,613 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 14:30:58 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-26 14:26:34 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.029 |  |
| 2026-04-26 14:24:43 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:11:41 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:10:53 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.054 |  |
| 2026-04-26 14:10:22 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:09:56 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-04-26 14:08:37 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-26 14:07:58 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-04-26 14:06:52 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:06:44 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -0.051 |  |
| 2026-04-26 14:06:34 | Katharagama (Menik Ganga) | 0.96 | 🟢 Normal | -0.282 |  |
| 2026-04-26 14:05:24 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:05:15 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:04:55 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-04-26 14:04:49 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-26 14:04:26 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-26 14:04:08 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:04:01 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-26 14:03:49 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:03:45 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-26 14:03:08 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.016 |  |
| 2026-04-26 14:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.040 |  |
| 2026-04-26 14:02:11 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | -0.050 |  |
| 2026-04-26 14:02:10 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-26 14:01:59 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:01:53 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | -0.021 |  |
| 2026-04-26 14:01:50 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.027 |  |
| 2026-04-26 14:01:46 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:01:39 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:01:31 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:01:26 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:01:20 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:01:19 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:01:04 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:01:01 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -0.022 |  |
| 2026-04-26 14:00:58 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-04-26 14:00:57 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 14:30:58 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-26 14:04:49 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-26 14:04:26 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-26 14:04:01 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-26 14:02:10 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-26 14:08:37 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-26 14:01:26 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:05:15 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:01:59 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:03:49 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:01:20 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:06:52 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:00:57 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:11:41 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:24:43 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:01:19 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:05:24 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-26 13:02:21 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:01:04 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:01:46 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:10:22 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:04:08 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:01:31 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:01:39 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-04-26 14:09:56 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-04-26 14:03:45 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-26 14:00:58 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-04-26 14:03:08 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.016 |  |
| 2026-04-26 14:04:55 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-04-26 14:07:58 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-04-26 14:01:53 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | -0.021 |  |
| 2026-04-26 14:01:01 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -0.022 |  |
| 2026-04-26 14:01:50 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.027 |  |
| 2026-04-26 14:26:34 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.029 |  |
| 2026-04-26 14:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.040 |  |
| 2026-04-26 14:02:11 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | -0.050 |  |
| 2026-04-26 14:06:44 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -0.051 |  |
| 2026-04-26 14:10:53 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.054 |  |
| 2026-04-26 14:06:34 | Katharagama (Menik Ganga) | 0.96 | 🟢 Normal | -0.282 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)