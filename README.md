# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_01:08:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,547 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 01:08:13 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-05-10 01:07:48 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.069 |  |
| 2026-05-10 01:06:42 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-05-10 01:06:20 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.046 |  |
| 2026-05-10 01:05:33 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.009 |  |
| 2026-05-10 01:05:11 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-05-10 01:04:57 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-10 01:04:52 | Wellawaya (Kirindi Oya) | 3.00 | 🟢 Normal | -0.079 |  |
| 2026-05-10 01:04:22 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.041 |  |
| 2026-05-10 01:04:10 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-05-10 01:03:24 | Moragaswewa (Deduru Oya) | 3.70 | 🟢 Normal | -0.030 |  |
| 2026-05-10 01:02:41 | Glencourse (Kelani Ganga) | 9.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 01:02:38 | Nakkala (Kumbukkan Oya) | 2.55 | 🟢 Normal | -0.088 |  |
| 2026-05-10 01:02:36 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-05-10 01:02:35 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.023 |  |
| 2026-05-10 01:02:23 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-10 01:02:00 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.060 |  |
| 2026-05-10 01:01:53 | Thaldena (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.169 |  |
| 2026-05-10 01:01:47 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.043 |  |
| 2026-05-10 01:01:42 | Thanamalwila (Kirindi Oya) | 1.99 | 🟢 Normal | -0.024 |  |
| 2026-05-10 01:01:21 | Kuda Oya (Kirindi Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-05-10 01:01:13 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.103 |  |
| 2026-05-10 01:01:07 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-10 01:01:06 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-10 01:00:46 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-10 01:00:33 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:59:56 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:45:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | -4.800 |  |
| 2026-05-10 00:44:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.98 | 🟢 Normal | -4.800 |  |
| 2026-05-10 00:17:52 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | -0.050 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 18:02:49 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-10 01:01:06 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-10 01:00:46 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-10 01:01:07 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-10 01:02:41 | Glencourse (Kelani Ganga) | 9.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 00:01:22 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-10 01:02:23 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-10 01:08:13 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:59:56 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-10 01:00:33 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 01:04:57 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:02:17 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:03:44 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-10 01:01:21 | Kuda Oya (Kirindi Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-05-10 01:05:33 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.009 |  |
| 2026-05-10 01:04:10 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-05-10 01:05:11 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-05-10 00:04:49 | Katharagama (Menik Ganga) | 1.60 | 🟢 Normal | -0.011 |  |
| 2026-05-10 00:02:12 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.011 |  |
| 2026-05-10 01:02:36 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-05-10 01:02:35 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.023 |  |
| 2026-05-10 01:01:42 | Thanamalwila (Kirindi Oya) | 1.99 | 🟢 Normal | -0.024 |  |
| 2026-05-10 00:09:52 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | -0.028 |  |
| 2026-05-10 01:03:24 | Moragaswewa (Deduru Oya) | 3.70 | 🟢 Normal | -0.030 |  |
| 2026-05-10 01:04:22 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.041 |  |
| 2026-05-10 01:01:47 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.043 |  |
| 2026-05-10 01:06:20 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.046 |  |
| 2026-05-10 00:17:52 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | -0.050 |  |
| 2026-05-09 18:00:42 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | -0.051 |  |
| 2026-05-10 01:02:00 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.060 |  |
| 2026-05-10 01:07:48 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.069 |  |
| 2026-05-10 01:04:52 | Wellawaya (Kirindi Oya) | 3.00 | 🟢 Normal | -0.079 |  |
| 2026-05-09 18:04:22 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | -0.081 |  |
| 2026-05-10 01:02:38 | Nakkala (Kumbukkan Oya) | 2.55 | 🟢 Normal | -0.088 |  |
| 2026-05-10 00:02:59 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.097 |  |
| 2026-05-10 01:01:13 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.103 |  |
| 2026-05-10 00:06:28 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.107 |  |
| 2026-05-10 01:01:53 | Thaldena (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.169 |  |
| 2026-05-10 00:45:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | -4.800 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)