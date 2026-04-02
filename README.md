# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_06:24:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **113,879 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 06:24:07 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:23:17 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | -0.001 |  |
| 2026-04-02 06:20:21 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-02 06:09:37 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-02 06:07:26 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:07:26 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:06:43 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.086 |  |
| 2026-04-02 06:06:38 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-04-02 06:06:25 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:06:16 | Kithulgala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-04-02 06:06:10 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:05:54 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:05:41 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-02 06:05:35 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.128 |  |
| 2026-04-02 06:05:08 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.087 |  |
| 2026-04-02 06:04:01 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:03:51 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:03:36 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 06:03:31 | Badalgama (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:03:25 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 06:03:14 | Ellagawa (Kalu Ganga) | 3.70 | 🟢 Normal | -0.010 |  |
| 2026-04-02 06:02:48 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.036 |  |
| 2026-04-02 06:02:47 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:02:39 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:02:36 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:02:19 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:02:13 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-04-02 06:02:02 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:01:54 | Weraganthota (Mahaweli Ganga) | -2.09 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-02 06:01:52 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:01:41 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:01:36 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.096 |  |
| 2026-04-02 06:01:33 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:01:22 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:01:13 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:01:11 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-02 06:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.07 | 🟢 Normal | -0.764 |  |
| 2026-04-02 06:00:55 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:00:51 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:50:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.21 | 🟢 Normal | -0.764 |  |
| 2026-04-02 05:38:29 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 06:02:13 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-04-02 06:06:16 | Kithulgala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-04-02 06:01:54 | Weraganthota (Mahaweli Ganga) | -2.09 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-02 06:01:11 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-02 06:09:37 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-02 06:03:25 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 06:03:36 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 06:05:41 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-02 06:20:21 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-02 06:02:19 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:01:13 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:24:07 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:07:26 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:01:22 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:00:51 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:01:41 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:02:02 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:03:51 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:07:26 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:01:33 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:06:25 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:02:47 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:02:39 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:04:01 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:03:31 | Badalgama (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:06:10 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:00:55 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:01:52 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:05:54 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:23:17 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | -0.001 |  |
| 2026-04-01 18:05:01 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-04-02 06:06:38 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-04-02 06:03:14 | Ellagawa (Kalu Ganga) | 3.70 | 🟢 Normal | -0.010 |  |
| 2026-04-02 06:02:48 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.036 |  |
| 2026-04-02 06:06:43 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.086 |  |
| 2026-04-02 06:05:08 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.087 |  |
| 2026-04-02 06:01:36 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.096 |  |
| 2026-04-02 06:05:35 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.128 |  |
| 2026-04-02 06:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.07 | 🟢 Normal | -0.764 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)