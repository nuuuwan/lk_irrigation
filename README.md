# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_07:11:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **195,917 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 07:11:09 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.002 |  |
| 2026-07-03 07:11:08 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:08:57 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:08:45 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:08:37 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 07:07:30 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.038 |  |
| 2026-07-03 07:07:28 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:07:24 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | -0.019 |  |
| 2026-07-03 07:07:02 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:07:00 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:06:38 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 07:05:47 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-07-03 07:05:35 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-03 07:05:31 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-07-03 07:04:43 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:04:27 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.028 |  |
| 2026-07-03 07:03:25 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 07:03:25 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 07:03:21 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.040 |  |
| 2026-07-03 07:02:38 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-07-03 07:02:30 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | -0.010 |  |
| 2026-07-03 07:02:22 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.050 |  |
| 2026-07-03 07:02:19 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.062 |  |
| 2026-07-03 07:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.060 |  |
| 2026-07-03 07:02:01 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:01:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:01:41 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-07-03 07:01:37 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.011 |  |
| 2026-07-03 07:01:26 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.029 |  |
| 2026-07-03 07:01:23 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:01:10 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:00:42 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:00:36 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:00:18 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.024 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 07:08:37 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 07:06:38 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 07:03:25 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 07:03:25 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 07:05:35 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-03 07:11:09 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.002 |  |
| 2026-07-03 07:00:42 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:01:23 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:01:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:11:08 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:01:58 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-03 06:01:14 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:01:10 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:04:43 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:07:28 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:08:45 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:02:01 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-03 06:04:56 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:08:57 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:07:00 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:00:36 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:07:02 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-03 05:37:09 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.007 |  |
| 2026-07-03 07:01:41 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-07-03 06:06:38 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-07-03 07:02:38 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-07-03 07:05:31 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-07-03 07:02:30 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | -0.010 |  |
| 2026-07-03 07:05:47 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-07-03 07:01:37 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.011 |  |
| 2026-07-03 07:07:24 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | -0.019 |  |
| 2026-07-03 07:00:18 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.024 |  |
| 2026-07-03 07:04:27 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.028 |  |
| 2026-07-03 07:01:26 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.029 |  |
| 2026-07-03 07:07:30 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.038 |  |
| 2026-07-03 07:03:21 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.040 |  |
| 2026-07-03 07:02:22 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.050 |  |
| 2026-07-03 07:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.060 |  |
| 2026-07-03 07:02:19 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)