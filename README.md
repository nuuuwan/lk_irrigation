# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_14:21:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,684 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 14:21:21 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-04-16 14:19:50 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-16 14:16:42 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-04-16 14:16:40 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.017 |  |
| 2026-04-16 14:09:35 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:08:02 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.065 |  |
| 2026-04-16 14:07:48 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-16 14:06:53 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:05:54 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:05:52 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:05:34 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:05:11 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.010 |  |
| 2026-04-16 14:05:04 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:04:22 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-16 14:04:16 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-04-16 14:04:13 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-04-16 14:03:39 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-16 14:03:19 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-04-16 14:02:58 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:02:43 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:02:41 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-16 14:02:32 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:02:32 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-16 14:02:28 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | -0.013 |  |
| 2026-04-16 14:02:25 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:02:19 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:02:17 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-16 14:02:13 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-16 14:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.040 |  |
| 2026-04-16 14:02:10 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | -0.077 |  |
| 2026-04-16 14:02:04 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 14:02:03 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-16 14:01:45 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:01:27 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:00:57 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:00:52 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:00:31 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | -0.031 |  |
| 2026-04-16 14:00:18 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:59:58 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 14:04:13 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-04-16 14:02:03 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-16 14:19:50 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-16 14:02:17 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-16 14:03:39 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-16 14:02:41 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-16 14:04:22 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-16 14:02:13 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-16 14:02:04 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 14:02:43 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:00:18 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:00:57 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:01:45 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:00:52 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:02:19 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:02:32 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:09:35 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:02:25 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:59:58 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:05:04 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:02:58 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:06:53 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:05:34 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:05:54 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:05:52 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 14:21:21 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-04-16 14:16:42 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-04-16 14:04:16 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-04-16 14:05:11 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.010 |  |
| 2026-04-16 14:07:48 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-16 14:02:32 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-16 14:02:28 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | -0.013 |  |
| 2026-04-16 14:16:40 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.017 |  |
| 2026-04-16 14:03:19 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-04-16 13:00:42 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.020 |  |
| 2026-04-16 14:00:31 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | -0.031 |  |
| 2026-04-16 14:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.040 |  |
| 2026-04-16 14:08:02 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.065 |  |
| 2026-04-16 14:02:10 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)