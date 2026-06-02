# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--02_19:07:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **168,665 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 19:07:03 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:05:47 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-06-02 19:05:45 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.065 |  |
| 2026-06-02 19:05:20 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-02 19:05:15 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-02 19:05:05 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-06-02 19:04:54 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.009 |  |
| 2026-06-02 19:04:49 | Hanwella (Kelani Ganga) | 1.61 | 🟢 Normal | -0.029 |  |
| 2026-06-02 19:04:36 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 19:04:25 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-02 19:03:22 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-06-02 19:03:22 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:03:21 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.116 |  |
| 2026-06-02 19:03:18 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | -0.043 |  |
| 2026-06-02 19:03:03 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:02:52 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.030 |  |
| 2026-06-02 19:02:28 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:02:27 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:02:25 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 19:02:08 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-06-02 19:02:03 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:01:50 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-06-02 19:01:42 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-06-02 19:01:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.010 |  |
| 2026-06-02 19:01:04 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:01:03 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:00:55 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:00:55 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:00:19 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-02 18:21:34 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 18:02:38 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-06-02 18:06:43 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-06-02 18:05:17 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-02 19:05:15 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-02 19:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-02 19:05:20 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-02 19:04:36 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 19:02:25 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:00:19 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:02:03 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:01:04 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:03:22 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:01:03 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-02 18:00:09 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:04:25 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:00:55 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:03:03 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:07:03 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:02:27 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-02 18:04:24 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 18:21:34 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:00:55 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:02:28 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:04:54 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.009 |  |
| 2026-06-02 19:02:08 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-06-02 19:05:05 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-06-02 18:08:47 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-06-02 19:01:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.010 |  |
| 2026-06-02 19:01:50 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-06-02 19:01:42 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-06-02 19:03:22 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-06-02 19:04:49 | Hanwella (Kelani Ganga) | 1.61 | 🟢 Normal | -0.029 |  |
| 2026-06-02 19:02:52 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.030 |  |
| 2026-06-02 19:03:18 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | -0.043 |  |
| 2026-06-02 18:06:27 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.050 |  |
| 2026-06-02 19:05:47 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-06-02 19:05:45 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.065 |  |
| 2026-06-02 19:03:21 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.116 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)