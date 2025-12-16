# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--16_08:04:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,287 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 08:04:02 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2025-12-16 08:03:59 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 08:03:47 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-16 08:03:31 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-16 08:03:07 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 08:02:58 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-16 08:02:49 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | -0.042 |  |
| 2025-12-16 08:02:33 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-16 08:02:32 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.021 |  |
| 2025-12-16 08:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.040 |  |
| 2025-12-16 08:02:06 | Thanthirimale (Malwathu Oya) | 3.95 | 🟢 Normal | -0.080 |  |
| 2025-12-16 08:01:52 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | -0.020 |  |
| 2025-12-16 08:01:43 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-16 08:01:17 | Yaka Wewa (Ma Oya) | 1.62 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2025-12-16 08:01:05 | Horowpothana (Yan Oya) | 4.23 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2025-12-16 08:00:52 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.063 |  |
| 2025-12-16 08:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-16 08:00:26 | Manampitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-16 08:00:22 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 08:00:12 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.024 |  |
| 2025-12-16 07:54:06 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-16 07:28:57 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.007 |  |
| 2025-12-16 07:19:36 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | -0.042 |  |
| 2025-12-16 07:14:44 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-16 07:13:02 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.063 |  |
| 2025-12-16 07:11:28 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-16 07:11:05 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -24.000 |  |
| 2025-12-16 07:11:02 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -24.000 |  |
| 2025-12-16 07:11:00 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -24.000 |  |
| 2025-12-16 07:09:39 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | -0.029 |  |
| 2025-12-16 07:09:36 | Thanthirimale (Malwathu Oya) | 4.02 | 🟢 Normal | -0.080 |  |
| 2025-12-16 07:09:15 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.024 |  |
| 2025-12-16 07:08:28 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-16 07:07:25 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2025-12-16 07:07:15 | Weraganthota (Mahaweli Ganga) | -1.11 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-16 07:07:11 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-16 07:06:56 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-16 07:06:45 | Panadugama (Nilwala Ganga) | 2.91 | 🟢 Normal | -0.021 |  |
| 2025-12-16 07:06:31 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-16 07:06:07 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 08:01:05 | Horowpothana (Yan Oya) | 4.23 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2025-12-16 07:04:27 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2025-12-16 08:01:17 | Yaka Wewa (Ma Oya) | 1.62 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2025-12-16 07:07:15 | Weraganthota (Mahaweli Ganga) | -1.11 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-16 08:00:26 | Manampitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-16 07:14:44 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-16 07:04:47 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 08:03:07 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 08:02:58 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-16 08:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-16 07:11:28 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-16 08:03:31 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-16 08:03:47 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-16 08:01:43 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-16 08:02:33 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-16 07:01:55 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 08:00:22 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 08:03:59 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 07:06:07 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-16 07:08:28 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-16 07:54:06 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-16 07:03:19 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-16 07:05:15 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-16 07:28:57 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.007 |  |
| 2025-12-16 07:07:25 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2025-12-16 07:01:07 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.011 |  |
| 2025-12-16 07:05:16 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.019 |  |
| 2025-12-16 08:01:52 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | -0.020 |  |
| 2025-12-16 08:04:02 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2025-12-16 07:06:45 | Panadugama (Nilwala Ganga) | 2.91 | 🟢 Normal | -0.021 |  |
| 2025-12-16 08:02:32 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.021 |  |
| 2025-12-16 06:02:42 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.023 |  |
| 2025-12-16 08:00:12 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.024 |  |
| 2025-12-16 07:09:39 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | -0.029 |  |
| 2025-12-16 08:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.040 |  |
| 2025-12-16 08:02:49 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | -0.042 |  |
| 2025-12-16 08:00:52 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.063 |  |
| 2025-12-16 08:02:06 | Thanthirimale (Malwathu Oya) | 3.95 | 🟢 Normal | -0.080 |  |
| 2025-12-16 07:11:05 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -24.000 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)