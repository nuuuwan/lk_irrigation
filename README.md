# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_13:10:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,607 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 13:10:05 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-02-07 13:07:01 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:06:54 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:06:48 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:06:15 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.014 |  |
| 2026-02-07 13:06:05 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:05:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.27 | 🟢 Normal | -0.048 |  |
| 2026-02-07 13:05:18 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.063 |  |
| 2026-02-07 13:04:42 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.050 |  |
| 2026-02-07 13:04:33 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | -0.011 |  |
| 2026-02-07 13:04:12 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-07 13:03:58 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-07 13:03:42 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:03:37 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-02-07 13:03:36 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:03:28 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -0.114 |  |
| 2026-02-07 13:03:15 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:03:09 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-02-07 13:03:06 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-07 13:03:01 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:02:53 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-02-07 13:02:34 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-07 13:02:18 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:02:07 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 13:01:56 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:01:52 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:01:34 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.082 |  |
| 2026-02-07 13:01:24 | Manampitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-07 13:01:19 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:01:17 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.011 |  |
| 2026-02-07 13:01:10 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-07 13:00:52 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:00:35 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-07 12:22:42 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 13:02:53 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-02-07 13:04:12 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-07 13:01:24 | Manampitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-07 13:01:10 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-07 13:03:06 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-07 13:02:07 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 13:03:58 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-07 13:03:15 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:01:19 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:00:52 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:01:56 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:01:52 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:07:01 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:00:35 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:03:36 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:06:54 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:03:01 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:02:18 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:06:05 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:03:42 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:06:48 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:05:35 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-07 13:03:37 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-02-07 13:02:34 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-07 13:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-07 13:01:17 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.011 |  |
| 2026-02-07 13:04:33 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | -0.011 |  |
| 2026-02-07 12:07:07 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.013 |  |
| 2026-02-07 13:06:15 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.014 |  |
| 2026-02-07 12:11:08 | Horowpothana (Yan Oya) | 2.62 | 🟢 Normal | -0.018 |  |
| 2026-02-07 13:03:09 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-02-07 12:03:28 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.022 |  |
| 2026-02-07 12:03:34 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.040 |  |
| 2026-02-07 13:10:05 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-02-07 13:05:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.27 | 🟢 Normal | -0.048 |  |
| 2026-02-07 13:04:42 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.050 |  |
| 2026-02-07 13:05:18 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.063 |  |
| 2026-02-07 13:01:34 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.082 |  |
| 2026-02-07 13:03:28 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -0.114 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)