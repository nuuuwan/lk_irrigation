# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--30_20:15:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **193,751 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 20:15:54 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:14:27 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.008 |  |
| 2026-06-30 20:12:51 | Ellagawa (Kalu Ganga) | 7.45 | 🟢 Normal | -0.103 |  |
| 2026-06-30 20:11:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.96 | 🟢 Normal | -0.039 |  |
| 2026-06-30 20:08:21 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-06-30 20:08:02 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:07:22 | Baddegama (Gin Ganga) | 2.40 | 🟢 Normal | -0.049 |  |
| 2026-06-30 20:06:59 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-06-30 20:06:18 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.033 |  |
| 2026-06-30 20:06:14 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-30 20:05:45 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.058 |  |
| 2026-06-30 20:05:45 | Rathnapura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.109 |  |
| 2026-06-30 20:05:16 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 20:04:31 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:04:14 | Putupaula (Kalu Ganga) | 1.66 | 🟢 Normal | -0.030 |  |
| 2026-06-30 20:03:57 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-06-30 20:03:43 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:03:11 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:03:08 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-30 20:03:07 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-06-30 20:03:02 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:02:58 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | -0.040 |  |
| 2026-06-30 20:02:42 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-30 20:02:36 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.050 |  |
| 2026-06-30 20:02:26 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:02:18 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-06-30 20:02:13 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:01:43 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:01:21 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:01:14 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:01:09 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:00:55 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:00:42 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:00:39 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:00:14 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 20:06:14 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-30 20:03:08 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-30 20:02:42 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-30 20:05:16 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 20:03:11 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:02:26 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:01:43 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:01:21 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:08:02 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-30 18:08:51 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:03:05 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:02:13 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:01:14 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:00:39 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:01:09 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:03:02 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:15:54 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-30 18:02:00 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:00:55 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:03:43 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:00:42 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-30 20:14:27 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.008 |  |
| 2026-06-30 20:08:21 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-06-30 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-06-30 20:03:07 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-06-30 20:02:18 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-06-30 20:03:57 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-06-30 20:06:59 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-06-30 20:00:14 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.020 |  |
| 2026-06-30 19:06:11 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.028 |  |
| 2026-06-30 20:04:14 | Putupaula (Kalu Ganga) | 1.66 | 🟢 Normal | -0.030 |  |
| 2026-06-30 20:06:18 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.033 |  |
| 2026-06-30 20:11:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.96 | 🟢 Normal | -0.039 |  |
| 2026-06-30 20:02:58 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | -0.040 |  |
| 2026-06-30 20:07:22 | Baddegama (Gin Ganga) | 2.40 | 🟢 Normal | -0.049 |  |
| 2026-06-30 20:02:36 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.050 |  |
| 2026-06-30 20:05:45 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.058 |  |
| 2026-06-30 20:12:51 | Ellagawa (Kalu Ganga) | 7.45 | 🟢 Normal | -0.103 |  |
| 2026-06-30 20:05:45 | Rathnapura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.109 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)