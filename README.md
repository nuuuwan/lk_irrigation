# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--09_23:32:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **175,077 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 23:32:19 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-09 23:21:28 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.008 |  |
| 2026-06-09 23:11:12 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-06-09 23:09:51 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | -0.019 |  |
| 2026-06-09 23:09:11 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-09 23:08:32 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.037 |  |
| 2026-06-09 23:07:00 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-06-09 23:06:50 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-06-09 23:06:49 | Glencourse (Kelani Ganga) | 11.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-09 23:05:58 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-06-09 23:05:40 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:05:22 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:05:19 | Putupaula (Kalu Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-06-09 23:05:05 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.063 |  |
| 2026-06-09 23:04:29 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:04:29 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:04:25 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:04:03 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:03:55 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:03:22 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:03:19 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:03:08 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-06-09 23:02:53 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-09 23:02:51 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:02:24 | Hanwella (Kelani Ganga) | 3.01 | 🟢 Normal | -0.030 |  |
| 2026-06-09 23:02:11 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-09 23:02:10 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | -0.020 |  |
| 2026-06-09 23:01:28 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-09 23:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-06-09 23:01:08 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 23:00:10 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 23:07:00 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-06-09 23:32:19 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-09 23:06:49 | Glencourse (Kelani Ganga) | 11.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-09 23:01:28 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-09 23:09:11 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-09 23:02:11 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-09 23:02:53 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-09 23:01:08 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 23:05:40 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:03:22 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:04:29 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-09 22:01:44 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:00:10 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-09 18:03:19 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:04:25 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:03:19 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:03:55 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:04:03 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-09 22:11:07 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:04:29 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:05:22 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 18:12:11 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-09 22:03:56 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:02:51 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-09 23:21:28 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.008 |  |
| 2026-06-09 23:06:50 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-06-09 23:05:19 | Putupaula (Kalu Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-06-09 23:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-06-09 23:05:58 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-06-09 23:03:08 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-06-09 23:09:51 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | -0.019 |  |
| 2026-06-09 22:20:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | -0.019 |  |
| 2026-06-09 23:11:12 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-06-09 22:13:36 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-06-09 23:02:10 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | -0.020 |  |
| 2026-06-09 23:02:24 | Hanwella (Kelani Ganga) | 3.01 | 🟢 Normal | -0.030 |  |
| 2026-06-09 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.031 |  |
| 2026-06-09 23:08:32 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.037 |  |
| 2026-06-09 23:05:05 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)