# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--15_04:20:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,390 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 04:20:37 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.004 |  |
| 2026-02-15 04:13:21 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:11:26 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.009 |  |
| 2026-02-15 04:10:27 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.053 |  |
| 2026-02-15 04:08:18 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 04:07:52 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-15 04:07:12 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-15 04:07:00 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:05:47 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:05:34 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:05:33 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:04:46 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 8.780 | 🔺 Rising |
| 2026-02-15 04:04:32 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:04:03 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:03:55 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:03:53 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-02-15 04:03:24 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 8.780 | 🔺 Rising |
| 2026-02-15 04:03:15 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:03:10 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-15 04:02:57 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 8.780 | 🔺 Rising |
| 2026-02-15 04:02:56 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.223 |  |
| 2026-02-15 04:02:42 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:02:38 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-15 04:02:29 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 04:02:21 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | -0.011 |  |
| 2026-02-15 04:02:20 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-15 04:02:12 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.181 |  |
| 2026-02-15 04:01:51 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:01:29 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:01:10 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 04:00:50 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 04:04:46 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 8.780 | 🔺 Rising |
| 2026-02-15 00:07:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-02-15 04:07:12 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-15 04:07:52 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-15 03:04:07 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-15 04:01:10 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 04:00:50 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 18:02:04 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 04:02:29 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 04:08:18 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 04:20:37 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.004 |  |
| 2026-02-15 03:03:55 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:03:55 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:01:51 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:02:28 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:02:20 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:03:27 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:04:32 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:02:42 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:05:47 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:04:03 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:04:12 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:01:29 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:07:00 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:01:28 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:05:34 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:06:23 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:13:21 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:11:26 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.009 |  |
| 2026-02-15 04:02:38 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-15 04:03:10 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-15 04:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-15 04:02:21 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | -0.011 |  |
| 2026-02-15 04:03:53 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-02-15 03:04:47 | Padiyathalawa (Maduru Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-02-15 04:10:27 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.053 |  |
| 2026-02-15 04:02:12 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.181 |  |
| 2026-02-15 04:02:56 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.223 |  |
| 2026-02-15 03:06:48 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -504.000 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)