# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_08:07:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,077 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 08:07:56 | Magura (Kalu Ganga) | 4.35 | 🟡 Alert | -0.072 |  |
| 2026-06-13 08:07:19 | Giriulla (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:06:50 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:06:37 | Peradeniya (Mahaweli Ganga) | 2.57 | 🟢 Normal | -0.028 |  |
| 2026-06-13 08:06:09 | Thawalama (Gin Ganga) | 3.07 | 🟢 Normal | -0.131 |  |
| 2026-06-13 08:06:04 | Badalgama (Maha Oya) | 3.43 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-13 08:05:52 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | -0.049 |  |
| 2026-06-13 08:05:10 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-06-13 08:05:08 | Baddegama (Gin Ganga) | 3.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-13 08:04:50 | Rathnapura (Kalu Ganga) | 5.82 | 🟡 Alert | -0.071 |  |
| 2026-06-13 08:04:33 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:04:29 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.019 |  |
| 2026-06-13 08:04:25 | Holombuwa (Kelani Ganga) | 1.59 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-06-13 08:04:24 | Glencourse (Kelani Ganga) | 11.84 | 🟢 Normal | -0.040 |  |
| 2026-06-13 08:04:15 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:04:03 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:03:54 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:03:26 | Galgamuwa (Mee Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-06-13 08:03:15 | Hanwella (Kelani Ganga) | 4.06 | 🟢 Normal | -0.041 |  |
| 2026-06-13 08:03:04 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 08:02:56 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 08:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.38 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-06-13 08:02:31 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.054 |  |
| 2026-06-13 08:02:13 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-06-13 08:02:09 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-06-13 08:02:06 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-06-13 08:02:03 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -2.400 |  |
| 2026-06-13 08:01:53 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.030 |  |
| 2026-06-13 08:01:51 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:01:48 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:01:41 | Ellagawa (Kalu Ganga) | 8.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 08:01:33 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -2.400 |  |
| 2026-06-13 08:01:27 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-13 08:01:19 | Putupaula (Kalu Ganga) | 2.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 08:01:13 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:01:12 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:00:56 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:00:46 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:00:32 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-13 07:39:34 | Holombuwa (Kelani Ganga) | 1.53 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-06-13 07:26:33 | Pitabeddara (Nilwala Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-06-13 07:23:40 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 07:22:33 | Rathnapura (Kalu Ganga) | 5.87 | 🟡 Alert | -0.071 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 08:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.38 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-06-13 08:04:50 | Rathnapura (Kalu Ganga) | 5.82 | 🟡 Alert | -0.071 |  |
| 2026-06-13 08:07:56 | Magura (Kalu Ganga) | 4.35 | 🟡 Alert | -0.072 |  |
| 2026-06-13 08:04:25 | Holombuwa (Kelani Ganga) | 1.59 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-06-13 08:06:04 | Badalgama (Maha Oya) | 3.43 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-13 07:01:35 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-13 08:03:04 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 08:01:41 | Ellagawa (Kalu Ganga) | 8.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 07:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 07:06:23 | Dunamale (Aththanagalu Oya) | 3.28 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-13 08:05:08 | Baddegama (Gin Ganga) | 3.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-13 08:00:32 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-13 08:01:19 | Putupaula (Kalu Ganga) | 2.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 08:02:56 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 08:01:27 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-13 08:01:13 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:03:54 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:07:19 | Giriulla (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:00:46 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:06:50 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:04:03 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:04:15 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:04:33 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:00:56 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:01:51 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:05:10 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-06-13 08:02:06 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-06-13 08:03:26 | Galgamuwa (Mee Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-06-13 08:02:09 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-06-13 08:04:29 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.019 |  |
| 2026-06-13 08:06:37 | Peradeniya (Mahaweli Ganga) | 2.57 | 🟢 Normal | -0.028 |  |
| 2026-06-13 08:01:53 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.030 |  |
| 2026-06-13 08:02:13 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-06-13 08:04:24 | Glencourse (Kelani Ganga) | 11.84 | 🟢 Normal | -0.040 |  |
| 2026-06-13 08:03:15 | Hanwella (Kelani Ganga) | 4.06 | 🟢 Normal | -0.041 |  |
| 2026-06-13 08:05:52 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | -0.049 |  |
| 2026-06-13 08:02:31 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.054 |  |
| 2026-06-13 08:06:09 | Thawalama (Gin Ganga) | 3.07 | 🟢 Normal | -0.131 |  |
| 2026-06-13 08:02:03 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -2.400 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)