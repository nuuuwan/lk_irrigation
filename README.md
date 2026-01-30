# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--30_15:11:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **59,827 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 15:11:08 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-30 15:10:33 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:08:35 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:08:32 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:08:12 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:07:36 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-30 15:07:02 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:06:41 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-30 15:06:02 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-30 15:05:48 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-01-30 15:05:30 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:05:14 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-30 15:05:13 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.009 |  |
| 2026-01-30 15:05:12 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:04:26 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-30 15:03:51 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:03:44 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 15:03:26 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-30 15:03:26 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-01-30 15:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.19 | 🟢 Normal | -0.029 |  |
| 2026-01-30 15:03:10 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:03:10 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:03:02 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:02:58 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:02:55 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:02:47 | Padiyathalawa (Maduru Oya) | 0.71 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-01-30 15:02:29 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-30 15:02:15 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:02:07 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-30 15:02:01 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 15:01:55 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:01:52 | Manampitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:01:26 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:01:23 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-30 15:01:10 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:01:08 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:00:42 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.133 |  |
| 2026-01-30 15:00:11 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-30 14:28:22 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:18:14 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.023 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 15:02:47 | Padiyathalawa (Maduru Oya) | 0.71 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-01-30 15:03:26 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-30 15:02:29 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-30 15:00:11 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-30 15:11:08 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-30 15:04:26 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-30 15:01:23 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-30 15:05:14 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-30 15:02:01 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 15:03:44 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 15:06:02 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-30 15:07:36 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-30 15:01:26 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-30 14:00:54 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:03:51 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:03:10 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:05:12 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:02:15 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:02:58 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:08:35 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:01:08 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:08:12 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:03:02 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:01:10 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:05:30 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:01:52 | Manampitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:07:02 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:10:33 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:02:55 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:01:55 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:08:32 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:05:13 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.009 |  |
| 2026-01-30 15:06:41 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-30 15:03:26 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-01-30 15:02:07 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-30 15:05:48 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-01-30 14:04:52 | Thawalama (Gin Ganga) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-01-30 15:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.19 | 🟢 Normal | -0.029 |  |
| 2026-01-30 15:00:42 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)