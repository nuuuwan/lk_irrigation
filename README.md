# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--04_08:18:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **36,234 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 08:18:48 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.092 |  |
| 2026-01-04 08:16:51 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:16:48 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:15:55 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:14:40 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-01-04 08:12:38 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.008 |  |
| 2026-01-04 08:11:08 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:10:19 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-01-04 08:09:22 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:08:20 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:08:17 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.182 |  |
| 2026-01-04 08:07:25 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:06:25 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-04 08:06:22 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.061 |  |
| 2026-01-04 08:05:47 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:05:34 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:04:40 | Weraganthota (Mahaweli Ganga) | -1.72 | 🟢 Normal | -0.058 |  |
| 2026-01-04 08:04:40 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-04 08:03:40 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-04 08:03:40 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-01-04 08:03:39 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-01-04 08:03:34 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:03:25 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:03:17 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 08:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.083 |  |
| 2026-01-04 08:03:07 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:03:05 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-01-04 08:02:23 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:02:14 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-04 08:02:12 | Galgamuwa (Mee Oya) | 2.62 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-04 08:02:11 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:02:00 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:01:56 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.158 |  |
| 2026-01-04 08:01:49 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:01:40 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-04 08:01:31 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:01:17 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:01:07 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:01:03 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:00:42 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | -0.023 |  |
| 2026-01-04 08:00:22 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 08:03:39 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-01-04 08:14:40 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-01-04 08:03:40 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-01-04 08:02:12 | Galgamuwa (Mee Oya) | 2.62 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-04 08:02:14 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-04 08:06:25 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-04 08:04:40 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-04 08:03:40 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-04 08:03:17 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 08:01:49 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:01:31 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:11:08 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:05:34 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:02:11 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:15:55 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:02:23 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:01:07 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:03:07 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:02:00 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:16:51 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:01:17 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:07:25 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:03:34 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:01:03 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:08:20 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:05:47 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:09:22 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-04 08:12:38 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.008 |  |
| 2026-01-04 08:01:40 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-04 08:00:22 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-01-04 08:03:05 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-01-04 08:00:42 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | -0.023 |  |
| 2026-01-04 08:10:19 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-01-04 08:04:40 | Weraganthota (Mahaweli Ganga) | -1.72 | 🟢 Normal | -0.058 |  |
| 2026-01-04 08:06:22 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.061 |  |
| 2026-01-04 08:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.083 |  |
| 2026-01-04 08:18:48 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.092 |  |
| 2026-01-04 08:01:56 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.158 |  |
| 2026-01-04 08:08:17 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.182 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)