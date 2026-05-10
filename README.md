# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_22:26:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,365 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 22:26:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.033 |  |
| 2026-05-10 22:22:48 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-05-10 22:12:43 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-05-10 22:11:08 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-10 22:08:10 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-10 22:07:02 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-05-10 22:06:48 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-10 22:06:47 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.028 |  |
| 2026-05-10 22:06:43 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-10 22:06:30 | Dunamale (Aththanagalu Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-05-10 22:05:46 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-10 22:05:28 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.041 |  |
| 2026-05-10 22:04:32 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 22:04:22 | Peradeniya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-10 22:04:08 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-05-10 22:03:33 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-05-10 22:03:32 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-10 22:03:26 | Moragaswewa (Deduru Oya) | 1.45 | 🟢 Normal | -0.032 |  |
| 2026-05-10 22:03:20 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-05-10 22:03:03 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-10 22:02:24 | Thanamalwila (Kirindi Oya) | 2.89 | 🟢 Normal | 0.956 | 🔺 Rising |
| 2026-05-10 22:02:24 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-10 22:02:13 | Katharagama (Menik Ganga) | 1.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-10 22:02:13 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-05-10 22:02:10 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-10 22:02:05 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-10 22:01:40 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.042 |  |
| 2026-05-10 22:01:35 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | -0.021 |  |
| 2026-05-10 22:01:22 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.033 |  |
| 2026-05-10 22:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-05-10 22:01:18 | Kuda Oya (Kirindi Oya) | 4.41 | 🟢 Normal | 1.417 | 🔺 Rising |
| 2026-05-10 22:01:10 | Wellawaya (Kirindi Oya) | 4.04 | 🟢 Normal | 0.689 | 🔺 Rising |
| 2026-05-10 22:01:08 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-05-10 22:01:05 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-10 22:00:59 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-10 22:00:51 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.035 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 22:01:18 | Kuda Oya (Kirindi Oya) | 4.41 | 🟢 Normal | 1.417 | 🔺 Rising |
| 2026-05-10 22:02:24 | Thanamalwila (Kirindi Oya) | 2.89 | 🟢 Normal | 0.956 | 🔺 Rising |
| 2026-05-10 22:01:10 | Wellawaya (Kirindi Oya) | 4.04 | 🟢 Normal | 0.689 | 🔺 Rising |
| 2026-05-10 22:12:43 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-05-10 22:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-05-10 22:22:48 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-05-10 22:03:32 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-10 22:01:08 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-05-10 22:02:24 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-10 22:06:43 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-10 22:04:22 | Peradeniya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-10 22:06:48 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-10 22:03:03 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-10 22:08:10 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-10 22:02:13 | Katharagama (Menik Ganga) | 1.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-10 22:02:05 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-10 22:05:46 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-10 22:04:32 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 22:02:10 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:06:14 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-10 22:11:08 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-10 22:01:05 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-10 22:00:59 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-10 22:06:30 | Dunamale (Aththanagalu Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:01:26 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 22:02:13 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-05-10 22:03:33 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-05-10 22:07:02 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-05-10 22:03:20 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-05-10 18:03:02 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.020 |  |
| 2026-05-10 22:04:08 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-05-10 22:01:35 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | -0.021 |  |
| 2026-05-10 22:06:47 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.028 |  |
| 2026-05-10 22:03:26 | Moragaswewa (Deduru Oya) | 1.45 | 🟢 Normal | -0.032 |  |
| 2026-05-10 22:01:22 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.033 |  |
| 2026-05-10 22:26:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.033 |  |
| 2026-05-10 22:00:51 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.035 |  |
| 2026-05-10 22:05:28 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.041 |  |
| 2026-05-10 22:01:40 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.042 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)