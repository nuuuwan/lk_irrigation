# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_14:28:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,050 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 14:28:28 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | -0.014 |  |
| 2026-05-01 14:16:27 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | -0.009 |  |
| 2026-05-01 14:10:04 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-01 14:09:00 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:08:51 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.056 |  |
| 2026-05-01 14:07:59 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:06:19 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-01 14:06:02 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.048 |  |
| 2026-05-01 14:05:59 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.058 |  |
| 2026-05-01 14:05:53 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:05:35 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:05:30 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:05:20 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:05:06 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-05-01 14:05:00 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.015 |  |
| 2026-05-01 14:04:51 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | -0.020 |  |
| 2026-05-01 14:04:51 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | -0.075 |  |
| 2026-05-01 14:04:41 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:04:20 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:04:10 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-01 14:03:48 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:03:41 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-01 14:03:25 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:03:12 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-05-01 14:02:58 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:02:58 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-01 14:02:54 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:02:41 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-05-01 14:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | -0.020 |  |
| 2026-05-01 14:02:04 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-01 14:02:03 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.012 |  |
| 2026-05-01 14:01:54 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:01:26 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -4.767 |  |
| 2026-05-01 14:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-05-01 14:01:04 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:00:41 | Thanthirimale (Malwathu Oya) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-05-01 14:00:40 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.033 |  |
| 2026-05-01 14:00:29 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-05-01 13:59:16 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 14:00:29 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-05-01 14:10:04 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-01 14:02:58 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-01 14:04:10 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-01 14:06:19 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-01 14:03:41 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-01 14:05:53 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:02:54 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:03:48 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:01:54 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:59:16 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:05:30 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:09:00 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:02:58 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:05:35 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:04:20 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:05:20 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:01:04 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:07:59 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:04:41 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:03:25 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-01 14:16:27 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | -0.009 |  |
| 2026-05-01 14:02:04 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-01 14:00:41 | Thanthirimale (Malwathu Oya) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-05-01 14:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-05-01 14:02:41 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-05-01 14:05:06 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-05-01 14:02:03 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.012 |  |
| 2026-05-01 14:28:28 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | -0.014 |  |
| 2026-05-01 14:05:00 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.015 |  |
| 2026-05-01 14:04:51 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | -0.020 |  |
| 2026-05-01 14:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | -0.020 |  |
| 2026-05-01 14:03:12 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-05-01 14:00:40 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.033 |  |
| 2026-05-01 14:06:02 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.048 |  |
| 2026-05-01 14:08:51 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.056 |  |
| 2026-05-01 14:05:59 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.058 |  |
| 2026-05-01 14:04:51 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | -0.075 |  |
| 2026-05-01 14:01:26 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -4.767 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)