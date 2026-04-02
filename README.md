# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_09:08:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **113,989 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 09:08:09 | Badalgama (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:08:05 | Hanwella (Kelani Ganga) | 0.23 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-02 09:07:30 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.030 |  |
| 2026-04-02 09:07:23 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-02 09:07:20 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:07:03 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | -0.020 |  |
| 2026-04-02 09:05:39 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:04:25 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:04:22 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 09:04:13 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.019 |  |
| 2026-04-02 09:03:28 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 09:03:23 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:02:58 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 09:02:55 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.021 |  |
| 2026-04-02 09:02:45 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-02 09:02:43 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.023 |  |
| 2026-04-02 09:02:33 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.152 |  |
| 2026-04-02 09:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:02:31 | Putupaula (Kalu Ganga) | 0.18 | 🟢 Normal | -0.125 |  |
| 2026-04-02 09:02:28 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-02 09:02:25 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:02:13 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:01:56 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:01:55 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:01:49 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:01:35 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.022 |  |
| 2026-04-02 09:01:32 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:01:12 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-04-02 09:01:12 | Ellagawa (Kalu Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:00:51 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-02 09:00:49 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-04-02 09:00:35 | Nawalapitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-04-02 09:00:26 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-02 08:34:19 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:17:46 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:17:32 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.044 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 09:00:35 | Nawalapitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-04-02 09:08:05 | Hanwella (Kelani Ganga) | 0.23 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-02 09:02:28 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-02 09:00:26 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-02 09:00:51 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-02 09:07:23 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-02 09:02:58 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 09:03:28 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 09:04:22 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 08:12:41 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-02 09:01:56 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:01:49 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:05:39 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:01:32 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:02:25 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:17:46 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:04:25 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:01:12 | Ellagawa (Kalu Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:04:57 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:01:55 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:06:35 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:08:09 | Badalgama (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:07:20 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:09:40 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:03:23 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:02:13 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:02:45 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-02 09:01:12 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-04-02 09:00:49 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-04-02 09:04:13 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.019 |  |
| 2026-04-02 09:07:03 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | -0.020 |  |
| 2026-04-02 09:02:55 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.021 |  |
| 2026-04-02 09:01:35 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.022 |  |
| 2026-04-02 09:02:43 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.023 |  |
| 2026-04-02 09:07:30 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.030 |  |
| 2026-04-02 08:17:32 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.044 |  |
| 2026-04-02 09:02:31 | Putupaula (Kalu Ganga) | 0.18 | 🟢 Normal | -0.125 |  |
| 2026-04-02 09:02:33 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)