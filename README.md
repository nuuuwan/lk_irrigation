# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--15_14:09:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,778 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 14:09:44 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-02-15 14:09:11 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -36.000 |  |
| 2026-02-15 14:09:10 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | -36.000 |  |
| 2026-02-15 14:06:31 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | -0.081 |  |
| 2026-02-15 14:05:29 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-15 14:05:12 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-15 14:05:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.050 |  |
| 2026-02-15 14:04:17 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-15 14:04:05 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:04:00 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.078 |  |
| 2026-02-15 14:03:54 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-15 14:03:41 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-02-15 14:03:37 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:03:33 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.051 |  |
| 2026-02-15 14:03:33 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:03:15 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:03:14 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-02-15 14:03:06 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 14:03:02 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.052 |  |
| 2026-02-15 14:03:00 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:02:50 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:02:35 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:02:34 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:02:32 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:02:31 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-02-15 14:02:19 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.022 |  |
| 2026-02-15 14:02:13 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:01:44 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.053 |  |
| 2026-02-15 14:01:41 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-15 14:01:36 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-15 14:01:35 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-02-15 14:01:18 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:01:08 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:01:07 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.010 |  |
| 2026-02-15 14:01:00 | Manampitiya (Mahaweli Ganga) | 2.55 | 🟢 Normal | -0.050 |  |
| 2026-02-15 14:00:49 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:00:49 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:00:33 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:00:31 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 14:01:41 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-15 14:03:54 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-15 14:05:29 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-15 14:04:17 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-15 14:03:06 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 14:03:37 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:00:33 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:00:49 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:02:35 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:02:32 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:02:50 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:03:33 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:03:00 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:00:49 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:01:08 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:02:13 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:04:05 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:00:31 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:03:15 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:01:18 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:02:34 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-15 14:09:44 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-02-15 14:05:12 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-15 14:01:07 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.010 |  |
| 2026-02-15 14:01:35 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-02-15 14:01:36 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-15 14:03:14 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-02-15 14:03:41 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-02-15 14:02:19 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.022 |  |
| 2026-02-15 13:03:39 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.030 |  |
| 2026-02-15 14:02:31 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-02-15 14:01:00 | Manampitiya (Mahaweli Ganga) | 2.55 | 🟢 Normal | -0.050 |  |
| 2026-02-15 14:05:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.050 |  |
| 2026-02-15 14:03:33 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.051 |  |
| 2026-02-15 14:03:02 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.052 |  |
| 2026-02-15 14:01:44 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.053 |  |
| 2026-02-15 14:04:00 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.078 |  |
| 2026-02-15 14:06:31 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | -0.081 |  |
| 2026-02-15 14:09:11 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)