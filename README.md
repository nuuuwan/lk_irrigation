# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_08:05:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **222,715 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 08:05:55 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.050 |  |
| 2026-08-02 08:05:11 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-02 08:04:56 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-02 08:04:51 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.156 |  |
| 2026-08-02 08:04:31 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.033 |  |
| 2026-08-02 08:04:29 | Hanwella (Kelani Ganga) | 2.59 | 🟢 Normal | -0.150 |  |
| 2026-08-02 08:04:09 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.049 |  |
| 2026-08-02 08:03:53 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-02 08:03:30 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 08:03:08 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-02 08:02:54 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.061 |  |
| 2026-08-02 08:02:50 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-02 08:02:34 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.579 | 🔺 Rising |
| 2026-08-02 08:02:20 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.021 |  |
| 2026-08-02 08:02:16 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-02 08:02:06 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | -0.117 |  |
| 2026-08-02 08:01:37 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-02 08:01:26 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 08:01:25 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-08-02 08:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-02 08:01:11 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 08:01:11 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-08-02 08:01:11 | Putupaula (Kalu Ganga) | 1.21 | 🟢 Normal | -0.108 |  |
| 2026-08-02 08:01:07 | Ellagawa (Kalu Ganga) | 6.08 | 🟢 Normal | -0.101 |  |
| 2026-08-02 08:00:53 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 08:00:39 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-02 07:32:16 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 07:18:28 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.013 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 08:02:34 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.579 | 🔺 Rising |
| 2026-08-02 08:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-02 06:03:19 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-08-02 08:04:56 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-02 08:03:30 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 08:01:26 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 08:01:11 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 08:01:11 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-08-02 08:00:39 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-02 07:11:05 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-02 08:00:53 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 07:16:01 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 07:01:00 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 08:03:08 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-02 07:15:55 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-02 07:12:20 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-08-02 07:32:16 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 08:02:16 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-02 08:03:53 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-02 08:05:11 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-02 08:02:50 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-02 07:13:42 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-02 08:01:37 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-02 07:13:59 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.008 |  |
| 2026-08-02 08:01:25 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-08-02 07:07:30 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-08-02 08:02:20 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.021 |  |
| 2026-08-02 08:04:31 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.033 |  |
| 2026-08-02 07:08:51 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.037 |  |
| 2026-08-02 07:03:32 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | -0.049 |  |
| 2026-08-02 08:04:09 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.049 |  |
| 2026-08-02 08:05:55 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.050 |  |
| 2026-08-02 08:02:54 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.061 |  |
| 2026-08-02 08:01:07 | Ellagawa (Kalu Ganga) | 6.08 | 🟢 Normal | -0.101 |  |
| 2026-08-02 08:01:11 | Putupaula (Kalu Ganga) | 1.21 | 🟢 Normal | -0.108 |  |
| 2026-08-02 08:02:06 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | -0.117 |  |
| 2026-08-02 08:04:29 | Hanwella (Kelani Ganga) | 2.59 | 🟢 Normal | -0.150 |  |
| 2026-08-02 08:04:51 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.156 |  |
| 2026-08-02 07:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.221 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)