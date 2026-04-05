# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_22:38:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,199 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 22:38:11 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:13:32 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:13:31 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:13:29 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:12:53 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.018 |  |
| 2026-04-05 22:12:18 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:11:16 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:07:44 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.028 |  |
| 2026-04-05 22:06:50 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-05 22:06:33 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:06:10 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.140 |  |
| 2026-04-05 22:06:07 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.028 |  |
| 2026-04-05 22:05:20 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-05 22:04:57 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:04:12 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.040 |  |
| 2026-04-05 22:03:55 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 22:03:34 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:03:28 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.035 |  |
| 2026-04-05 22:02:46 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-04-05 22:02:41 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:02:39 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:02:37 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-05 22:02:21 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.023 |  |
| 2026-04-05 22:02:14 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:02:05 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:02:03 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:02:00 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.230 |  |
| 2026-04-05 22:01:59 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-05 22:01:53 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:01:41 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:01:21 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.021 |  |
| 2026-04-05 22:01:15 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.032 |  |
| 2026-04-05 22:01:08 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:00:43 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 22:00:40 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-05 22:00:39 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-05 22:00:35 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:59:41 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 22:00:40 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-05 22:00:39 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-05 22:05:20 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-05 22:06:50 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-05 21:59:41 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 22:03:55 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 22:00:43 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 22:00:35 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:02:39 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:38:11 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:02:03 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:13:32 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:02:05 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:11:16 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:06:33 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:04:57 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:12:18 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:02:41 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:01:08 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:02:14 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:01:41 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:01:53 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:01:59 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:02:03 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-05 22:02:37 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-05 22:12:53 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.018 |  |
| 2026-04-05 22:02:46 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-04-05 22:01:21 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.021 |  |
| 2026-04-05 22:02:21 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.023 |  |
| 2026-04-05 22:06:07 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.028 |  |
| 2026-04-05 22:07:44 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.028 |  |
| 2026-04-05 22:01:15 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.032 |  |
| 2026-04-05 22:03:28 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.035 |  |
| 2026-04-05 22:04:12 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.040 |  |
| 2026-04-05 18:02:13 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.050 |  |
| 2026-04-05 21:08:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.081 |  |
| 2026-04-05 18:02:28 | Thanthirimale (Malwathu Oya) | 2.42 | 🟢 Normal | -0.088 |  |
| 2026-04-05 22:06:10 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.140 |  |
| 2026-04-05 22:02:00 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.230 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)