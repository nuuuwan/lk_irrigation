# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--30_23:34:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **193,861 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 23:34:38 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:34:16 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:10:03 | Putupaula (Kalu Ganga) | 1.68 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-30 23:09:09 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:09:07 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | -0.027 |  |
| 2026-06-30 23:08:45 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:07:24 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-30 23:07:09 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | -0.109 |  |
| 2026-06-30 23:06:57 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -0.041 |  |
| 2026-06-30 23:06:43 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-06-30 23:05:58 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.028 |  |
| 2026-06-30 23:05:57 | Glencourse (Kelani Ganga) | 10.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 23:05:52 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.042 |  |
| 2026-06-30 23:05:35 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-30 23:05:14 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:05:08 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-06-30 23:04:37 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.039 |  |
| 2026-06-30 23:04:34 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-06-30 23:04:12 | Rathnapura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.068 |  |
| 2026-06-30 23:03:56 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:03:55 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-06-30 23:03:48 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-30 23:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | 504.000 | 🔺 Rising |
| 2026-06-30 23:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.38 | 🟢 Normal | 504.000 | 🔺 Rising |
| 2026-06-30 23:03:05 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-30 23:02:58 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 23:02:53 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:02:50 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-30 23:02:22 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-06-30 23:02:07 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-06-30 23:01:54 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:01:21 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:01:11 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:01:07 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-30 23:00:55 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-06-30 23:00:52 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:00:33 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 23:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | 504.000 | 🔺 Rising |
| 2026-06-30 23:01:07 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-30 23:03:05 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-30 23:02:50 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-30 23:05:35 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-30 23:10:03 | Putupaula (Kalu Ganga) | 1.68 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-30 23:07:24 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-30 23:05:57 | Glencourse (Kelani Ganga) | 10.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 23:02:58 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 23:03:56 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:34:38 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:01:21 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:00:52 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-30 18:08:51 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:09:09 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:01:11 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:02:53 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:01:54 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:00:33 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-30 18:02:00 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:05:14 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-30 22:03:37 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:12:20 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.005 |  |
| 2026-06-30 23:05:08 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-06-30 23:03:48 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-30 23:02:07 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-06-30 23:02:22 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-06-30 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-06-30 23:03:55 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-06-30 23:00:55 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-06-30 23:06:43 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-06-30 23:04:34 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-06-30 23:09:07 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | -0.027 |  |
| 2026-06-30 23:05:58 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.028 |  |
| 2026-06-30 23:04:37 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.039 |  |
| 2026-06-30 23:06:57 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -0.041 |  |
| 2026-06-30 23:05:52 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.042 |  |
| 2026-06-30 23:04:12 | Rathnapura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.068 |  |
| 2026-06-30 23:07:09 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | -0.109 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)