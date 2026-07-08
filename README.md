# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--08_18:07:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **200,850 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-08 18:07:52 | Thalgahagoda (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.009 |  |
| 2026-07-08 18:07:39 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:06:59 | Glencourse (Kelani Ganga) | 9.35 | 🟢 Normal | -0.074 |  |
| 2026-07-08 18:05:51 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.049 |  |
| 2026-07-08 18:05:48 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:05:45 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-07-08 18:05:31 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-08 18:05:18 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:04:30 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:04:20 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:03:32 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:03:17 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.029 |  |
| 2026-07-08 18:03:13 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:02:58 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:02:44 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-07-08 18:02:43 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-07-08 18:02:38 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.043 |  |
| 2026-07-08 18:02:30 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.040 |  |
| 2026-07-08 18:02:28 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | -0.010 |  |
| 2026-07-08 18:02:19 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:02:10 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-07-08 18:01:50 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:01:48 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.020 |  |
| 2026-07-08 18:01:44 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.012 |  |
| 2026-07-08 18:01:30 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.023 |  |
| 2026-07-08 18:01:29 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.021 |  |
| 2026-07-08 18:01:17 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:01:08 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-08 18:00:56 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:00:50 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:00:42 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:00:36 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:00:31 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-08 18:02:10 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-07-08 18:05:45 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-07-08 18:01:08 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-08 18:05:31 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-08 18:02:19 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:00:36 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:01:17 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:00:56 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:05:48 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:00:31 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-08 17:08:44 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:02:58 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:01:50 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:05:18 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:02:30 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:04:30 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-07-08 17:05:09 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-07-08 17:04:56 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:00:42 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:03:32 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:00:50 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:04:20 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:03:13 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:01:29 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-08 17:12:36 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:07:39 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:07:52 | Thalgahagoda (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.009 |  |
| 2026-07-08 18:02:28 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | -0.010 |  |
| 2026-07-08 18:02:44 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-07-08 18:01:44 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.012 |  |
| 2026-07-08 18:01:48 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.020 |  |
| 2026-07-08 18:02:43 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-07-08 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.021 |  |
| 2026-07-08 18:01:30 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.023 |  |
| 2026-07-08 18:03:17 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.029 |  |
| 2026-07-08 18:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.040 |  |
| 2026-07-08 18:02:38 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.043 |  |
| 2026-07-08 18:05:51 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.049 |  |
| 2026-07-08 18:06:59 | Glencourse (Kelani Ganga) | 9.35 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)