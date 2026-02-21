# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_18:08:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,288 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 18:08:42 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:08:11 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-02-21 18:06:43 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.655 | 🔺 Rising |
| 2026-02-21 18:06:02 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-02-21 18:05:42 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.035 |  |
| 2026-02-21 18:05:22 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 18:05:18 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.098 |  |
| 2026-02-21 18:05:11 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-21 18:05:06 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:05:03 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-02-21 18:04:40 | Nakkala (Kumbukkan Oya) | 2.98 | 🟢 Normal | 1.588 | 🔺 Rising |
| 2026-02-21 18:04:40 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-21 18:04:38 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | 0.728 | 🔺 Rising |
| 2026-02-21 18:04:26 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.525 | 🔺 Rising |
| 2026-02-21 18:04:26 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-21 18:03:51 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:47 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:35 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:08 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:04 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-21 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | -0.020 |  |
| 2026-02-21 18:02:48 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-21 18:02:46 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:02:45 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | -0.010 |  |
| 2026-02-21 18:02:40 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:02:27 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.424 | 🔺 Rising |
| 2026-02-21 18:02:17 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:02:12 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-02-21 18:02:12 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-21 18:02:05 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.343 | 🔺 Rising |
| 2026-02-21 18:01:33 | Manampitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | -0.030 |  |
| 2026-02-21 18:01:28 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-02-21 18:01:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.13 | 🟢 Normal | -0.062 |  |
| 2026-02-21 18:01:16 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:01:03 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-02-21 18:00:43 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:00:31 | Padiyathalawa (Maduru Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-02-21 18:00:12 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | -0.068 |  |
| 2026-02-21 17:53:34 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-21 17:43:11 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:42:52 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 18:04:40 | Nakkala (Kumbukkan Oya) | 2.98 | 🟢 Normal | 1.588 | 🔺 Rising |
| 2026-02-21 18:04:38 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | 0.728 | 🔺 Rising |
| 2026-02-21 18:06:43 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.655 | 🔺 Rising |
| 2026-02-21 18:04:26 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.525 | 🔺 Rising |
| 2026-02-21 18:02:27 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.424 | 🔺 Rising |
| 2026-02-21 18:02:05 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.343 | 🔺 Rising |
| 2026-02-21 18:08:11 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-02-21 18:05:03 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-02-21 18:02:12 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-02-21 18:01:03 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-02-21 18:01:28 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-02-21 18:06:02 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-02-21 18:04:26 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-21 17:53:34 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-21 18:02:12 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-21 18:03:04 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-21 18:05:11 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-21 18:04:40 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-21 17:06:59 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-21 18:05:22 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 18:05:06 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:01:16 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:35 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:47 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:08:42 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:02:46 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:51 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:02:17 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:08 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:00:43 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:02:48 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-21 18:02:45 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | -0.010 |  |
| 2026-02-21 18:00:31 | Padiyathalawa (Maduru Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-02-21 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | -0.020 |  |
| 2026-02-21 18:01:33 | Manampitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | -0.030 |  |
| 2026-02-21 18:05:42 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.035 |  |
| 2026-02-21 18:01:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.13 | 🟢 Normal | -0.062 |  |
| 2026-02-21 18:00:12 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | -0.068 |  |
| 2026-02-21 18:05:18 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)