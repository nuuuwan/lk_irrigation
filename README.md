# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_10:11:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **203,241 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 10:11:15 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:10:42 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-07-11 10:10:34 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.018 |  |
| 2026-07-11 10:08:42 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:08:00 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:07:39 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:07:26 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:07:17 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:06:44 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:06:41 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.028 |  |
| 2026-07-11 10:05:53 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:05:46 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:05:06 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.029 |  |
| 2026-07-11 10:03:58 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:03:56 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:03:46 | Hanwella (Kelani Ganga) | 1.56 | 🟢 Normal | -0.071 |  |
| 2026-07-11 10:03:36 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:03:26 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-07-11 10:03:22 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-07-11 10:03:15 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:03:09 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:03:08 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-07-11 10:03:07 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 10:03:05 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 10:02:51 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-07-11 10:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 10:02:40 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.030 |  |
| 2026-07-11 10:02:38 | Ellagawa (Kalu Ganga) | 4.72 | 🟢 Normal | -0.020 |  |
| 2026-07-11 10:02:37 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.021 |  |
| 2026-07-11 10:02:33 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:02:26 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-07-11 10:01:50 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:01:38 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-07-11 10:01:24 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:00:54 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:00:41 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:00:24 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:00:21 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 10:03:22 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-07-11 10:03:26 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-07-11 10:10:42 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-07-11 10:03:07 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 10:03:05 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 10:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 10:02:33 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:07:17 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:11:15 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:03:15 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-11 09:08:14 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:07:26 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:01:50 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:05:53 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:03:56 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:05:46 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:00:54 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:08:42 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:08:00 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:07:39 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:00:24 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:03:36 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:03:58 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:06:44 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:00:41 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:03:09 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 10:03:08 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-07-11 10:02:26 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-07-11 10:02:51 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-07-11 10:01:38 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-07-11 10:10:34 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.018 |  |
| 2026-07-11 10:02:38 | Ellagawa (Kalu Ganga) | 4.72 | 🟢 Normal | -0.020 |  |
| 2026-07-11 10:02:37 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.021 |  |
| 2026-07-11 10:06:41 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.028 |  |
| 2026-07-11 10:05:06 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.029 |  |
| 2026-07-11 10:02:40 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.030 |  |
| 2026-07-11 10:00:21 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.041 |  |
| 2026-07-11 10:03:46 | Hanwella (Kelani Ganga) | 1.56 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)