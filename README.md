# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_21:19:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **179,473 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 21:19:28 | Panadugama (Nilwala Ganga) | 3.56 | 🟢 Normal | 27.907 | 🔺 Rising |
| 2026-06-14 21:17:19 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 27.907 | 🔺 Rising |
| 2026-06-14 21:13:32 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.035 |  |
| 2026-06-14 21:07:48 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-06-14 21:07:32 | Glencourse (Kelani Ganga) | 10.81 | 🟢 Normal | -0.040 |  |
| 2026-06-14 21:06:54 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.035 |  |
| 2026-06-14 21:06:49 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.012 |  |
| 2026-06-14 21:06:34 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.033 |  |
| 2026-06-14 21:06:32 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | -0.030 |  |
| 2026-06-14 21:05:51 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-06-14 21:05:27 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 27.907 | 🔺 Rising |
| 2026-06-14 21:05:25 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:04:02 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | -0.029 |  |
| 2026-06-14 21:03:50 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-06-14 21:03:45 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:03:41 | Ellagawa (Kalu Ganga) | 7.74 | 🟢 Normal | -0.059 |  |
| 2026-06-14 21:03:39 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.021 |  |
| 2026-06-14 21:03:37 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-06-14 21:03:36 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:03:28 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.185 |  |
| 2026-06-14 21:03:24 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:03:21 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.042 |  |
| 2026-06-14 21:03:10 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:03:09 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:03:04 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-06-14 21:02:41 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:02:41 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | -0.010 |  |
| 2026-06-14 21:02:23 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:02:17 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:02:16 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:02:10 | Hanwella (Kelani Ganga) | 3.08 | 🟢 Normal | -0.040 |  |
| 2026-06-14 21:01:58 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:01:46 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.059 |  |
| 2026-06-14 21:01:45 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:01:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.01 | 🟡 Alert | -0.034 |  |
| 2026-06-14 21:01:18 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:00:18 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:59:10 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 21:01:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.01 | 🟡 Alert | -0.034 |  |
| 2026-06-14 21:19:28 | Panadugama (Nilwala Ganga) | 3.56 | 🟢 Normal | 27.907 | 🔺 Rising |
| 2026-06-14 21:05:51 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-06-14 21:00:18 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:03:45 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:02:16 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:01:18 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:03:24 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:03:10 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:03:37 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:05:25 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:03:36 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:01:45 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:02:17 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:03:09 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:02:41 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:01:58 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-14 21:02:23 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-14 18:04:23 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.009 |  |
| 2026-06-14 21:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-06-14 18:01:41 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-06-14 21:02:41 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | -0.010 |  |
| 2026-06-14 21:03:50 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-06-14 21:06:49 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.012 |  |
| 2026-06-14 18:03:42 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-06-14 21:07:48 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-06-14 21:03:04 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-06-14 21:03:39 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.021 |  |
| 2026-06-14 21:04:02 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | -0.029 |  |
| 2026-06-14 21:06:32 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | -0.030 |  |
| 2026-06-14 21:06:34 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.033 |  |
| 2026-06-14 21:06:54 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.035 |  |
| 2026-06-14 21:13:32 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.035 |  |
| 2026-06-14 21:07:32 | Glencourse (Kelani Ganga) | 10.81 | 🟢 Normal | -0.040 |  |
| 2026-06-14 21:02:10 | Hanwella (Kelani Ganga) | 3.08 | 🟢 Normal | -0.040 |  |
| 2026-06-14 21:03:21 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.042 |  |
| 2026-06-14 21:03:41 | Ellagawa (Kalu Ganga) | 7.74 | 🟢 Normal | -0.059 |  |
| 2026-06-14 21:01:46 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.059 |  |
| 2026-06-14 21:03:28 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.185 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)