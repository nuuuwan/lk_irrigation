# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_20:29:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,125 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 20:29:42 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:13:45 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.041 |  |
| 2026-04-05 20:11:59 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-04-05 20:11:45 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:11:24 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:09:51 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-04-05 20:08:39 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.142 |  |
| 2026-04-05 20:08:20 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.048 |  |
| 2026-04-05 20:07:58 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.066 |  |
| 2026-04-05 20:07:29 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-04-05 20:07:26 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.020 |  |
| 2026-04-05 20:07:23 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-05 20:06:01 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 20:05:45 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:05:23 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.043 |  |
| 2026-04-05 20:04:43 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:04:25 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:04:20 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:04:18 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:04:01 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:03:22 | Manampitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.030 |  |
| 2026-04-05 20:03:17 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-04-05 20:03:15 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-05 20:03:11 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:02:48 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:02:34 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | -0.031 |  |
| 2026-04-05 20:02:23 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-04-05 20:02:19 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:02:18 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:01:58 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:01:54 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.061 |  |
| 2026-04-05 20:01:16 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-04-05 20:01:14 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 20:07:23 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-05 20:03:15 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-05 20:06:01 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 20:01:14 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:04:20 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:01:58 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:29:42 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:11:24 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:02:18 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:04:43 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:04:18 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:03:11 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:04:25 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:02:19 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:05:45 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:11:45 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:02:48 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:04:01 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:18:54 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.008 |  |
| 2026-04-05 20:11:59 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-04-05 20:03:17 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:02:03 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-05 20:09:51 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:01:22 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-04-05 20:02:23 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-04-05 20:07:29 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-04-05 20:07:26 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.020 |  |
| 2026-04-05 20:01:16 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-04-05 20:03:22 | Manampitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.030 |  |
| 2026-04-05 20:02:34 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | -0.031 |  |
| 2026-04-05 20:13:45 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.041 |  |
| 2026-04-05 20:05:23 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.043 |  |
| 2026-04-05 20:08:20 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.048 |  |
| 2026-04-05 18:02:13 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.050 |  |
| 2026-04-05 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.23 | 🟢 Normal | -0.053 |  |
| 2026-04-05 20:01:54 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.061 |  |
| 2026-04-05 20:07:58 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.066 |  |
| 2026-04-05 18:02:28 | Thanthirimale (Malwathu Oya) | 2.42 | 🟢 Normal | -0.088 |  |
| 2026-04-05 20:08:39 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.142 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)