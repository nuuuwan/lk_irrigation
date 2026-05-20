# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_09:11:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **156,836 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 09:11:18 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:09:11 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-05-20 09:09:06 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-05-20 09:08:47 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.044 |  |
| 2026-05-20 09:08:13 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-20 09:07:13 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:07:08 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:06:14 | Moragaswewa (Deduru Oya) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-05-20 09:06:13 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.028 |  |
| 2026-05-20 09:05:34 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:05:30 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:04:22 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:04:18 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-05-20 09:04:08 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-05-20 09:03:54 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:03:48 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-20 09:03:43 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.060 |  |
| 2026-05-20 09:03:39 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:03:22 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | -0.051 |  |
| 2026-05-20 09:03:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:03:09 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-20 09:03:01 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.065 |  |
| 2026-05-20 09:02:55 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-20 09:02:47 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:02:38 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-05-20 09:02:34 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-20 09:02:33 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.010 |  |
| 2026-05-20 09:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-20 09:01:47 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:01:40 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:01:36 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-20 09:01:32 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:01:29 | Thanthirimale (Malwathu Oya) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-05-20 09:01:22 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:01:15 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.132 |  |
| 2026-05-20 09:01:08 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:00:24 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:00:23 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:00:22 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 09:03:48 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-20 09:03:09 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-20 09:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-20 09:02:55 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-20 09:01:36 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-20 09:08:13 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-20 09:01:08 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:00:23 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:03:39 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:01:47 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:04:22 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:00:22 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:05:30 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:05:34 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:11:18 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:01:40 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:01:22 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:02:47 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:07:13 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:03:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:07:08 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:03:54 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:01:32 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:00:24 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:09:11 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-05-20 09:04:18 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-05-20 09:04:08 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-05-20 09:09:06 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-05-20 09:02:38 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-05-20 09:02:34 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-20 09:02:33 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.010 |  |
| 2026-05-20 09:01:29 | Thanthirimale (Malwathu Oya) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-05-20 09:06:13 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.028 |  |
| 2026-05-20 09:06:14 | Moragaswewa (Deduru Oya) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-05-20 09:08:47 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.044 |  |
| 2026-05-20 09:03:22 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | -0.051 |  |
| 2026-05-20 09:03:43 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.060 |  |
| 2026-05-20 09:03:01 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.065 |  |
| 2026-05-20 09:01:15 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)