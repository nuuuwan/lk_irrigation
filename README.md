# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_19:07:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,683 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 19:07:50 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | -0.009 |  |
| 2026-04-27 19:07:47 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-27 19:07:45 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-04-27 19:07:38 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-04-27 19:07:37 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-27 19:07:26 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:06:30 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:06:13 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-04-27 19:05:49 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-27 19:05:22 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 19:04:32 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-27 19:04:25 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-27 19:04:24 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.040 |  |
| 2026-04-27 19:04:21 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:04:15 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:04:03 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-04-27 19:03:46 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-04-27 19:03:31 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:02:33 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.031 |  |
| 2026-04-27 19:02:26 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:02:20 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-04-27 19:02:19 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-27 19:02:16 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:01:51 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:01:46 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:01:39 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-27 19:01:36 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-04-27 19:01:34 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.061 |  |
| 2026-04-27 19:01:13 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:01:09 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:00:44 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:32:07 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:31:25 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.016 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 18:05:04 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-04-27 19:02:20 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-04-27 19:02:19 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-27 19:04:03 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-04-27 19:04:25 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-27 18:00:50 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-27 19:07:37 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-27 19:07:47 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-27 19:01:39 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-27 18:05:30 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 19:05:22 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 19:05:49 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-27 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:01:13 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:02:16 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:00:44 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:01:46 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:03:31 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:04:15 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:02:26 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:01:09 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:07:26 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:03:04 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:04:32 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:01:51 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:06:30 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:07:45 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-04-27 19:07:50 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | -0.009 |  |
| 2026-04-27 19:06:13 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-04-27 19:04:32 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-27 19:01:36 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-04-27 19:03:46 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-04-27 19:07:38 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-04-27 18:00:10 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-04-27 18:05:39 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.031 |  |
| 2026-04-27 19:02:33 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.031 |  |
| 2026-04-27 19:04:24 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.040 |  |
| 2026-04-27 19:01:34 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)