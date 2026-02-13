# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--13_09:07:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,797 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 09:07:40 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:06:17 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-13 09:06:16 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:06:03 | Rathnapura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.144 |  |
| 2026-02-13 09:04:50 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-02-13 09:04:42 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:04:23 | Dunamale (Aththanagalu Oya) | 0.29 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-13 09:04:12 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 09:04:07 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-13 09:04:07 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:03:59 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-13 09:03:57 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:03:50 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:03:37 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:03:24 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 09:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | -0.166 |  |
| 2026-02-13 09:03:18 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.088 |  |
| 2026-02-13 09:03:05 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-13 09:02:51 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-13 09:02:50 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:02:44 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-02-13 09:02:37 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:02:33 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-02-13 09:02:09 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:02:08 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-13 09:02:07 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:02:01 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:01:44 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.021 |  |
| 2026-02-13 09:01:33 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:01:32 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-02-13 09:01:32 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.090 |  |
| 2026-02-13 09:01:31 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-02-13 09:01:09 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:01:01 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:01:01 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-13 08:36:59 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:26:44 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:22:31 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-13 08:16:45 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.026 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 09:01:32 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-02-13 09:02:44 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-02-13 09:03:05 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-13 08:22:31 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-13 09:02:08 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-13 09:01:01 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-13 09:04:07 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-13 09:06:17 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-13 09:02:51 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-13 09:04:23 | Dunamale (Aththanagalu Oya) | 0.29 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-13 09:04:12 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 08:03:13 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 09:03:24 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 09:02:33 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-02-13 09:02:01 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:01:09 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:03:37 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:02:50 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:07:40 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:04:42 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:04:07 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:02:07 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:01:33 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:03:57 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:06:16 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:02:37 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:03:50 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:02:09 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:26:44 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:01:01 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-13 08:08:50 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 09:03:59 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-13 09:04:50 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-02-13 09:01:31 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-02-13 09:01:44 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.021 |  |
| 2026-02-13 09:03:18 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.088 |  |
| 2026-02-13 09:01:32 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.090 |  |
| 2026-02-13 09:06:03 | Rathnapura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.144 |  |
| 2026-02-13 09:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | -0.166 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)