# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_20:09:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,300 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 20:09:28 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:08:55 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.028 |  |
| 2026-06-06 20:08:21 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.048 |  |
| 2026-06-06 20:07:22 | Rathnapura (Kalu Ganga) | 2.88 | 🟢 Normal | -0.067 |  |
| 2026-06-06 20:06:50 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:06:47 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-06 20:06:31 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.020 |  |
| 2026-06-06 20:06:12 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-06 20:05:46 | Putupaula (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:05:42 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-06-06 20:05:37 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:05:35 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 20:05:14 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:04:58 | Hanwella (Kelani Ganga) | 3.22 | 🟢 Normal | -0.039 |  |
| 2026-06-06 20:04:57 | Peradeniya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 20:04:50 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.009 |  |
| 2026-06-06 20:04:28 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-06 20:04:20 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:04:16 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.13 | 🟢 Normal | -0.021 |  |
| 2026-06-06 20:04:04 | Dunamale (Aththanagalu Oya) | 2.88 | 🟢 Normal | -0.049 |  |
| 2026-06-06 20:04:00 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:03:43 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:03:33 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.019 |  |
| 2026-06-06 20:03:27 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-06-06 20:02:47 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.021 |  |
| 2026-06-06 20:02:47 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-06-06 20:02:39 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:02:15 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-06-06 20:02:09 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-06-06 20:01:51 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:01:47 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-06-06 20:01:46 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:01:26 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:01:23 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:01:05 | Ellagawa (Kalu Ganga) | 7.25 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 20:06:47 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-06 20:04:28 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-06 20:06:12 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-06 20:05:35 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 20:04:57 | Peradeniya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 18:06:04 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:02:39 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:04:00 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:05:14 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:01:26 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:02:07 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:03:43 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:05:37 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:01:23 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:04:16 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:05:46 | Putupaula (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:04:20 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:01:43 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:01:51 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:09:28 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:01:46 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:06:50 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:04:50 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.009 |  |
| 2026-06-06 20:05:42 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-06-06 20:01:47 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-06-06 20:03:27 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-06-06 20:02:47 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-06-06 20:03:33 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.019 |  |
| 2026-06-06 20:01:05 | Ellagawa (Kalu Ganga) | 7.25 | 🟢 Normal | -0.020 |  |
| 2026-06-06 20:06:31 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.020 |  |
| 2026-06-06 20:02:47 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.021 |  |
| 2026-06-06 20:02:09 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-06-06 20:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.13 | 🟢 Normal | -0.021 |  |
| 2026-06-06 20:08:55 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.028 |  |
| 2026-06-06 20:02:15 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-06-06 20:04:58 | Hanwella (Kelani Ganga) | 3.22 | 🟢 Normal | -0.039 |  |
| 2026-06-06 20:08:21 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.048 |  |
| 2026-06-06 20:04:04 | Dunamale (Aththanagalu Oya) | 2.88 | 🟢 Normal | -0.049 |  |
| 2026-06-06 20:07:22 | Rathnapura (Kalu Ganga) | 2.88 | 🟢 Normal | -0.067 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)