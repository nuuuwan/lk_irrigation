# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_06:28:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,035 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 06:28:09 | Galgamuwa (Mee Oya) | 1.26 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-07 06:10:08 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 06:09:54 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-07 06:07:34 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-05-07 06:06:41 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-07 06:06:40 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.100 |  |
| 2026-05-07 06:06:21 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.072 |  |
| 2026-05-07 06:05:56 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-07 06:05:49 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 06:05:33 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-07 06:04:38 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-07 06:04:28 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-07 06:04:27 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-07 06:04:26 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-05-07 06:04:20 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-07 06:04:19 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-07 06:04:14 | Glencourse (Kelani Ganga) | 11.34 | 🟢 Normal | -0.010 |  |
| 2026-05-07 06:04:13 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-07 06:04:07 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-05-07 06:04:05 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.101 |  |
| 2026-05-07 06:04:04 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.204 |  |
| 2026-05-07 06:04:03 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.280 |  |
| 2026-05-07 06:03:19 | Horowpothana (Yan Oya) | 2.96 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-05-07 06:03:11 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-07 06:02:27 | Hanwella (Kelani Ganga) | 1.98 | 🟢 Normal | 0.982 | 🔺 Rising |
| 2026-05-07 06:02:20 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-05-07 06:02:16 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.064 |  |
| 2026-05-07 06:02:11 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.021 |  |
| 2026-05-07 06:02:07 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-05-07 06:02:02 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.032 |  |
| 2026-05-07 06:01:55 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 06:01:50 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.091 |  |
| 2026-05-07 06:01:40 | Weraganthota (Mahaweli Ganga) | -2.69 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-07 06:01:39 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-07 06:01:17 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | -0.756 |  |
| 2026-05-07 06:01:00 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 06:00:37 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-05-07 06:00:31 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | 0.000 |  |
| 2026-05-07 05:58:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | -0.021 |  |
| 2026-05-07 05:50:58 | Thawalama (Gin Ganga) | 3.23 | 🟢 Normal | -0.756 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 06:02:27 | Hanwella (Kelani Ganga) | 1.98 | 🟢 Normal | 0.982 | 🔺 Rising |
| 2026-05-07 06:02:20 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-05-07 06:04:26 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-05-07 06:04:07 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-05-07 06:03:19 | Horowpothana (Yan Oya) | 2.96 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-05-07 06:00:37 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-05-07 06:07:34 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-05-07 06:28:09 | Galgamuwa (Mee Oya) | 1.26 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-07 06:03:11 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-07 06:04:20 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-07 06:04:27 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-07 06:01:40 | Weraganthota (Mahaweli Ganga) | -2.69 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-07 06:06:41 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-07 06:05:49 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 06:09:54 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-07 06:01:00 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 06:01:55 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 06:10:08 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 06:00:31 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | 0.000 |  |
| 2026-05-07 06:04:28 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-07 06:04:13 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-07 06:05:33 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-07 06:04:19 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-07 06:05:56 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-07 06:02:07 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:28 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-07 06:01:39 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-07 06:04:14 | Glencourse (Kelani Ganga) | 11.34 | 🟢 Normal | -0.010 |  |
| 2026-05-07 06:02:11 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.021 |  |
| 2026-05-07 05:58:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | -0.021 |  |
| 2026-05-07 06:02:02 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.032 |  |
| 2026-05-07 06:02:16 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.064 |  |
| 2026-05-07 06:06:21 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.072 |  |
| 2026-05-07 06:01:50 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.091 |  |
| 2026-05-07 06:06:40 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.100 |  |
| 2026-05-07 06:04:05 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.101 |  |
| 2026-05-07 06:04:04 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.204 |  |
| 2026-05-07 06:04:03 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.280 |  |
| 2026-05-07 06:01:17 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | -0.756 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)