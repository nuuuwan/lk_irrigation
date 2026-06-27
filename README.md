# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--27_23:20:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **191,154 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 23:20:35 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:16:28 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:12:13 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-06-27 23:11:38 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.023 |  |
| 2026-06-27 23:09:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:09:09 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:08:06 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:07:18 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:06:33 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:05:51 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2026-06-27 23:05:43 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-27 23:05:33 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-06-27 23:05:13 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-06-27 23:05:09 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:05:05 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:05:05 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-27 23:04:27 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-06-27 23:03:55 | Hanwella (Kelani Ganga) | 1.64 | 🟢 Normal | -0.029 |  |
| 2026-06-27 23:03:45 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-06-27 23:03:22 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-27 23:02:57 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:02:39 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:02:37 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-06-27 23:02:21 | Peradeniya (Mahaweli Ganga) | 2.11 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-06-27 23:02:07 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-27 23:01:54 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:01:50 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | -0.021 |  |
| 2026-06-27 23:01:48 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-27 23:01:09 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-27 23:01:01 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:00:48 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:00:31 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:00:17 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 23:05:51 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2026-06-27 23:05:13 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-06-27 23:02:21 | Peradeniya (Mahaweli Ganga) | 2.11 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-06-27 23:05:43 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-27 23:05:05 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-27 23:03:22 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-27 23:01:48 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-27 18:03:41 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:01:01 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:02:57 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:00:31 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-27 21:00:11 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:20:35 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:00:48 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 18:03:17 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:01:54 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:02:39 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:06:33 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:07:18 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:00:17 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:16:28 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 22:06:16 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:09:09 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:08:06 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:05:09 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-27 22:05:19 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:09:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-06-27 23:12:13 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-06-27 18:02:27 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-27 23:02:07 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-27 22:02:25 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-06-27 23:01:09 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-27 23:03:45 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-06-27 23:05:33 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-06-27 23:02:37 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-06-27 23:04:27 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-06-27 23:01:50 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | -0.021 |  |
| 2026-06-27 23:11:38 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.023 |  |
| 2026-06-27 23:03:55 | Hanwella (Kelani Ganga) | 1.64 | 🟢 Normal | -0.029 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)