# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--19_11:12:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **183,534 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 11:12:42 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | -0.014 |  |
| 2026-06-19 11:11:45 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | -0.021 |  |
| 2026-06-19 11:10:39 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:08:35 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-19 11:08:31 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-06-19 11:08:23 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-19 11:07:01 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:06:38 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.022 |  |
| 2026-06-19 11:06:18 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-06-19 11:06:10 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.015 |  |
| 2026-06-19 11:05:01 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:04:59 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:04:28 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.243 |  |
| 2026-06-19 11:04:21 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-06-19 11:04:20 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-19 11:04:12 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.022 |  |
| 2026-06-19 11:03:57 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:03:41 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:03:39 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-06-19 11:03:32 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:03:28 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.021 |  |
| 2026-06-19 11:03:15 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-06-19 11:03:07 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | -0.031 |  |
| 2026-06-19 11:03:02 | Rathnapura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.035 |  |
| 2026-06-19 11:03:00 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:02:38 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-19 11:02:31 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-06-19 11:02:19 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:02:01 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:02:01 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | -0.023 |  |
| 2026-06-19 11:01:44 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:01:44 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | -0.030 |  |
| 2026-06-19 11:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:01:12 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:01:05 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | -0.011 |  |
| 2026-06-19 11:00:59 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-06-19 11:00:13 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.020 |  |
| 2026-06-19 11:00:09 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 11:04:20 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-19 11:08:35 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-19 11:08:23 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-19 11:00:09 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:03:41 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:01:12 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:03:57 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:04:59 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:02:01 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:02:19 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:03:32 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:05:01 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:07:01 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:10:39 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:01:44 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:03:00 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 11:08:31 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-06-19 11:02:31 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-06-19 11:03:39 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-06-19 11:04:21 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-06-19 11:00:59 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-06-19 11:02:38 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-19 11:01:05 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | -0.011 |  |
| 2026-06-19 11:06:18 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-06-19 11:12:42 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | -0.014 |  |
| 2026-06-19 11:06:10 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.015 |  |
| 2026-06-19 11:00:13 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.020 |  |
| 2026-06-19 11:11:45 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | -0.021 |  |
| 2026-06-19 11:03:28 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.021 |  |
| 2026-06-19 11:06:38 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.022 |  |
| 2026-06-19 11:04:12 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.022 |  |
| 2026-06-19 11:02:01 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | -0.023 |  |
| 2026-06-19 11:03:15 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-06-19 11:01:44 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | -0.030 |  |
| 2026-06-19 11:03:07 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | -0.031 |  |
| 2026-06-19 11:03:02 | Rathnapura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.035 |  |
| 2026-06-19 11:04:28 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.243 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)