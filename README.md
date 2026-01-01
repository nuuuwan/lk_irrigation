# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--02_03:26:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,239 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 03:26:24 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:21:01 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.003 |  |
| 2026-01-02 03:17:35 | Horowpothana (Yan Oya) | 3.82 | 🟢 Normal | -0.013 |  |
| 2026-01-02 03:17:35 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:17:09 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:15:24 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:11:19 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-02 03:07:02 | Padiyathalawa (Maduru Oya) | 3.99 | 🟢 Normal | -0.261 |  |
| 2026-01-02 03:06:21 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.091 |  |
| 2026-01-02 03:06:06 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:05:41 | Katharagama (Menik Ganga) | 1.04 | 🟢 Normal | -0.120 |  |
| 2026-01-02 03:05:29 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-02 03:05:19 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-02 03:05:03 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-02 03:04:55 | Nakkala (Kumbukkan Oya) | 1.91 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-01-02 03:04:36 | Manampitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-02 03:04:28 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.422 |  |
| 2026-01-02 03:04:27 | Thanamalwila (Kirindi Oya) | 1.83 | 🟢 Normal | -0.052 |  |
| 2026-01-02 03:03:52 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:03:21 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 03:03:04 | Siyambalanduwa (Heda Oya) | 2.19 | 🟢 Normal | -0.055 |  |
| 2026-01-02 03:02:51 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-01-02 03:02:40 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-01-02 03:01:47 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:01:41 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-01-02 03:01:33 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:01:32 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:01:31 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:01:31 | Kuda Oya (Kirindi Oya) | 1.97 | 🟢 Normal | -0.029 |  |
| 2026-01-02 03:01:22 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:01:15 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:01:07 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:01:06 | Thaldena (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 03:00:57 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-02 02:49:03 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:45:44 | Katharagama (Menik Ganga) | 1.08 | 🟢 Normal | -0.120 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 03:02:51 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-01-02 03:04:55 | Nakkala (Kumbukkan Oya) | 1.91 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-01-02 03:11:19 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-02 03:04:36 | Manampitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-02 03:05:29 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-02 03:03:21 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 03:01:06 | Thaldena (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 03:03:52 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:09:46 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:06:06 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:01:33 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:17:35 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:01:15 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | 0.000 |  |
| 2026-01-02 02:15:00 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:01:22 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:01:47 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:01:07 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:15:24 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:26:24 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:00:46 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:21:01 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.003 |  |
| 2026-01-02 03:05:03 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-02 03:05:19 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-02 03:00:57 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-02 03:17:35 | Horowpothana (Yan Oya) | 3.82 | 🟢 Normal | -0.013 |  |
| 2026-01-02 02:02:54 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-01-01 18:02:09 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | -0.020 |  |
| 2026-01-02 03:02:40 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-01-02 03:01:41 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-01-02 03:01:31 | Kuda Oya (Kirindi Oya) | 1.97 | 🟢 Normal | -0.029 |  |
| 2026-01-01 20:14:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-01-02 00:11:06 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.038 |  |
| 2026-01-01 18:00:31 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.040 |  |
| 2026-01-02 03:04:27 | Thanamalwila (Kirindi Oya) | 1.83 | 🟢 Normal | -0.052 |  |
| 2026-01-02 03:03:04 | Siyambalanduwa (Heda Oya) | 2.19 | 🟢 Normal | -0.055 |  |
| 2026-01-02 03:06:21 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.091 |  |
| 2026-01-02 03:05:41 | Katharagama (Menik Ganga) | 1.04 | 🟢 Normal | -0.120 |  |
| 2026-01-02 03:07:02 | Padiyathalawa (Maduru Oya) | 3.99 | 🟢 Normal | -0.261 |  |
| 2026-01-02 03:04:28 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.422 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)