# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_19:16:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,233 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 19:16:01 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-11 19:12:42 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | -0.060 |  |
| 2025-12-11 19:09:51 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.020 |  |
| 2025-12-11 19:08:01 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 19:07:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | -0.019 |  |
| 2025-12-11 19:07:46 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-11 19:07:25 | Urawa (Nilwala Ganga) | 1.70 | 🟢 Normal | 0.744 | 🔺 Rising |
| 2025-12-11 19:06:03 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | -0.009 |  |
| 2025-12-11 19:05:55 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-11 19:05:54 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 19:05:07 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 19:04:43 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-11 19:04:43 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-11 19:04:41 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2025-12-11 19:04:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-11 19:04:33 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-11 19:04:31 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | 0.405 | 🔺 Rising |
| 2025-12-11 19:03:52 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-11 19:03:46 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 19:03:16 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-11 19:03:06 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.111 |  |
| 2025-12-11 19:03:04 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-11 19:02:38 | Panadugama (Nilwala Ganga) | 3.04 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-11 19:02:15 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.020 |  |
| 2025-12-11 19:01:52 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-11 19:01:48 | Padiyathalawa (Maduru Oya) | 3.50 | 🟢 Normal | 0.827 | 🔺 Rising |
| 2025-12-11 19:01:42 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-11 19:01:40 | Yaka Wewa (Ma Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-11 19:01:31 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-11 19:01:23 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 19:01:20 | Manampitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 19:01:19 | Horowpothana (Yan Oya) | 4.26 | 🟢 Normal | -0.042 |  |
| 2025-12-11 19:01:03 | Siyambalanduwa (Heda Oya) | 1.66 | 🟢 Normal | 0.283 | 🔺 Rising |
| 2025-12-11 18:26:44 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.049 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 19:01:48 | Padiyathalawa (Maduru Oya) | 3.50 | 🟢 Normal | 0.827 | 🔺 Rising |
| 2025-12-11 19:07:25 | Urawa (Nilwala Ganga) | 1.70 | 🟢 Normal | 0.744 | 🔺 Rising |
| 2025-12-11 19:04:31 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | 0.405 | 🔺 Rising |
| 2025-12-11 19:01:03 | Siyambalanduwa (Heda Oya) | 1.66 | 🟢 Normal | 0.283 | 🔺 Rising |
| 2025-12-11 15:01:10 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2025-12-11 19:04:43 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-11 19:04:41 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2025-12-11 19:02:38 | Panadugama (Nilwala Ganga) | 3.04 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-11 18:04:39 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-11 19:03:16 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-11 19:01:31 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-11 19:01:52 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-11 15:04:23 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-11 19:04:33 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-11 19:01:42 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-11 19:03:52 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-11 19:16:01 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-11 19:05:07 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 19:03:46 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 19:01:23 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 19:01:20 | Manampitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 15:11:23 | Moragaswewa (Deduru Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2025-12-11 19:03:04 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-11 19:01:40 | Yaka Wewa (Ma Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-11 19:07:46 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:02:22 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 19:04:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-11 19:05:55 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-11 19:08:01 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 19:05:54 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 19:04:43 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-11 19:06:03 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | -0.009 |  |
| 2025-12-11 19:07:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | -0.019 |  |
| 2025-12-11 19:02:15 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.020 |  |
| 2025-12-11 19:09:51 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.020 |  |
| 2025-12-11 18:02:46 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | -0.033 |  |
| 2025-12-11 19:01:19 | Horowpothana (Yan Oya) | 4.26 | 🟢 Normal | -0.042 |  |
| 2025-12-11 19:12:42 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | -0.060 |  |
| 2025-12-11 19:03:06 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)