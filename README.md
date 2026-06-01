# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--01_18:11:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **167,731 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 18:11:11 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-01 18:10:16 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:09:17 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.009 |  |
| 2026-06-01 18:09:07 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-06-01 18:07:52 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.117 |  |
| 2026-06-01 18:06:54 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.077 |  |
| 2026-06-01 18:06:35 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:05:37 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.021 |  |
| 2026-06-01 18:05:13 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:04:51 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:04:15 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.019 |  |
| 2026-06-01 18:04:11 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-01 18:04:03 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:03:58 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:03:57 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:03:55 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:03:28 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 18:03:26 | Hanwella (Kelani Ganga) | 1.91 | 🟢 Normal | -0.020 |  |
| 2026-06-01 18:03:14 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:03:00 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-06-01 18:02:59 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:02:54 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | -0.020 |  |
| 2026-06-01 18:02:29 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.023 |  |
| 2026-06-01 18:02:28 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:02:28 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.022 |  |
| 2026-06-01 18:02:22 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.050 |  |
| 2026-06-01 18:02:21 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | -0.021 |  |
| 2026-06-01 18:02:20 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.012 |  |
| 2026-06-01 18:02:15 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.011 |  |
| 2026-06-01 18:02:12 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-06-01 18:02:06 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:02:06 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:02:01 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-06-01 18:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:01:39 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-01 18:01:35 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:01:25 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:00:20 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:00:18 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:00:11 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 18:09:07 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-06-01 18:01:39 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-01 18:04:11 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-01 18:11:11 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-01 18:03:28 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 18:02:06 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:06:35 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:03:58 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:03:14 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:00:20 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:02:28 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:10:16 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:02:06 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:04:03 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:00:11 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:04:51 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:02:59 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:01:25 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:01:35 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:03:55 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:02:22 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:03:57 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:09:17 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.009 |  |
| 2026-06-01 18:03:00 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-06-01 18:02:12 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-06-01 18:02:01 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-06-01 18:02:15 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.011 |  |
| 2026-06-01 18:02:20 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.012 |  |
| 2026-06-01 18:04:15 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.019 |  |
| 2026-06-01 18:02:54 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | -0.020 |  |
| 2026-06-01 18:03:26 | Hanwella (Kelani Ganga) | 1.91 | 🟢 Normal | -0.020 |  |
| 2026-06-01 18:02:21 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | -0.021 |  |
| 2026-06-01 18:05:37 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.021 |  |
| 2026-06-01 18:02:28 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.022 |  |
| 2026-06-01 18:02:29 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.023 |  |
| 2026-06-01 18:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.050 |  |
| 2026-06-01 18:06:54 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.077 |  |
| 2026-06-01 18:07:52 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)