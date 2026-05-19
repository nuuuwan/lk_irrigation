# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_22:14:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **156,447 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 22:14:21 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-19 22:13:22 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:12:44 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:10:39 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | -0.019 |  |
| 2026-05-19 22:10:09 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | -0.019 |  |
| 2026-05-19 22:09:33 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:08:08 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | -0.018 |  |
| 2026-05-19 22:06:25 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.061 |  |
| 2026-05-19 22:06:10 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:05:41 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:05:38 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-05-19 22:05:21 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | -0.030 |  |
| 2026-05-19 22:04:57 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-19 22:04:30 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 22:03:51 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:03:46 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:03:40 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-05-19 22:03:34 | Moragaswewa (Deduru Oya) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-19 22:03:32 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.036 |  |
| 2026-05-19 22:03:28 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-19 22:03:11 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | 12.247 | 🔺 Rising |
| 2026-05-19 22:03:09 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:03:07 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-05-19 22:03:01 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:02:52 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:02:44 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.010 |  |
| 2026-05-19 22:02:17 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.021 |  |
| 2026-05-19 22:02:16 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-19 22:02:12 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-05-19 22:02:02 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:01:55 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.013 |  |
| 2026-05-19 22:01:48 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.011 |  |
| 2026-05-19 22:01:34 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | 12.247 | 🔺 Rising |
| 2026-05-19 22:01:03 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:00:40 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | -0.027 |  |
| 2026-05-19 22:00:37 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:00:31 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 22:03:11 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | 12.247 | 🔺 Rising |
| 2026-05-19 22:04:57 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-19 22:14:21 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-19 22:02:16 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-19 22:03:34 | Moragaswewa (Deduru Oya) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-19 22:04:30 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 18:04:04 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:00:37 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:01:03 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:00:31 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:05:41 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:03:48 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:03:46 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:13:22 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:03:51 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:02:52 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:02:02 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:09:33 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:03:01 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:06:10 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:12:44 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-19 22:03:40 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-05-19 22:03:28 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-19 22:05:38 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-05-19 22:03:07 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-05-19 22:02:44 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.010 |  |
| 2026-05-19 22:02:12 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-05-19 22:01:48 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.011 |  |
| 2026-05-19 22:01:55 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.013 |  |
| 2026-05-19 22:08:08 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | -0.018 |  |
| 2026-05-19 22:10:09 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | -0.019 |  |
| 2026-05-19 22:10:39 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | -0.019 |  |
| 2026-05-19 18:02:04 | Thanthirimale (Malwathu Oya) | 2.22 | 🟢 Normal | -0.021 |  |
| 2026-05-19 22:02:17 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.021 |  |
| 2026-05-19 22:00:40 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | -0.027 |  |
| 2026-05-19 22:05:21 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | -0.030 |  |
| 2026-05-19 22:03:32 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.036 |  |
| 2026-05-19 21:18:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.38 | 🟢 Normal | -0.052 |  |
| 2026-05-19 22:06:25 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)