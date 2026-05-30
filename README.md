# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_20:35:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **166,000 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 20:35:25 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:23:39 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:18:12 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:17:42 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:12:04 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:11:59 | Magura (Kalu Ganga) | 2.61 | 🟢 Normal | -0.028 |  |
| 2026-05-30 20:10:43 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | -0.024 |  |
| 2026-05-30 20:09:38 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:09:38 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:09:22 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.019 |  |
| 2026-05-30 20:09:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.13 | 🟡 Alert | -0.029 |  |
| 2026-05-30 20:08:50 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-05-30 20:07:58 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-05-30 20:07:55 | Dunamale (Aththanagalu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:06:51 | Rathnapura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-05-30 20:06:39 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.009 |  |
| 2026-05-30 20:05:47 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:05:32 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:04:57 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:04:32 | Baddegama (Gin Ganga) | 2.60 | 🟢 Normal | -0.040 |  |
| 2026-05-30 20:04:22 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-30 20:04:14 | Ellagawa (Kalu Ganga) | 7.02 | 🟢 Normal | -0.099 |  |
| 2026-05-30 20:03:58 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.060 |  |
| 2026-05-30 20:03:57 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-05-30 20:03:38 | Putupaula (Kalu Ganga) | 2.46 | 🟢 Normal | -0.012 |  |
| 2026-05-30 20:03:01 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 20:09:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.13 | 🟡 Alert | -0.029 |  |
| 2026-05-30 20:08:50 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-05-30 20:04:22 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-30 20:02:34 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 18:00:56 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:00:31 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:17:42 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:01:36 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:02:38 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:23:39 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:04:48 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:03:01 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:35:25 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:02:17 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:02:21 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:07:55 | Dunamale (Aththanagalu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:05:47 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:09:38 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:31 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:09:38 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:18:12 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:12:04 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:02:46 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 20:06:39 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.009 |  |
| 2026-05-30 20:06:51 | Rathnapura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-05-30 20:03:57 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-05-30 20:00:34 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-05-30 20:03:38 | Putupaula (Kalu Ganga) | 2.46 | 🟢 Normal | -0.012 |  |
| 2026-05-30 20:01:33 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.012 |  |
| 2026-05-30 20:07:58 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-05-30 20:09:22 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.019 |  |
| 2026-05-30 20:10:43 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | -0.024 |  |
| 2026-05-30 20:11:59 | Magura (Kalu Ganga) | 2.61 | 🟢 Normal | -0.028 |  |
| 2026-05-30 20:04:32 | Baddegama (Gin Ganga) | 2.60 | 🟢 Normal | -0.040 |  |
| 2026-05-30 20:03:58 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.060 |  |
| 2026-05-30 20:02:14 | Hanwella (Kelani Ganga) | 2.54 | 🟢 Normal | -0.070 |  |
| 2026-05-30 20:01:35 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.099 |  |
| 2026-05-30 20:04:14 | Ellagawa (Kalu Ganga) | 7.02 | 🟢 Normal | -0.099 |  |
| 2026-05-30 18:02:04 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -30.857 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)