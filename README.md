# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--11_09:12:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **176,325 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 09:12:15 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-11 09:09:24 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-11 09:08:03 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:07:39 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-11 09:07:23 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:06:46 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-11 09:06:37 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:06:30 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 09:06:08 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-11 09:06:06 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-11 09:05:57 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:05:39 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:05:34 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:05:28 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-06-11 09:04:04 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-11 09:03:38 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-11 09:03:32 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:03:21 | Ellagawa (Kalu Ganga) | 5.71 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-11 09:03:09 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-11 09:03:02 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-11 09:02:58 | Glencourse (Kelani Ganga) | 10.88 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:02:55 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:02:47 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:02:45 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.021 |  |
| 2026-06-11 09:02:37 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:02:34 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.029 |  |
| 2026-06-11 09:02:31 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:02:22 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:02:02 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:01:58 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:01:43 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.005 |  |
| 2026-06-11 09:01:34 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:01:26 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:01:05 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:00:30 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:00:23 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-06-11 09:00:23 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.061 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 09:06:08 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-11 09:00:23 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-11 09:06:06 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-11 09:09:24 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-11 09:04:04 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-11 09:12:15 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-11 09:06:46 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-11 09:03:38 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-11 09:03:21 | Ellagawa (Kalu Ganga) | 5.71 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-11 09:03:02 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-11 09:03:09 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-11 09:06:30 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 09:07:39 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-11 09:03:32 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:02:55 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:05:39 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:08:03 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:07:23 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:01:26 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:01:05 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:05:34 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:06:37 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:02:47 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:05:57 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:02:58 | Glencourse (Kelani Ganga) | 10.88 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:02:31 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:02:22 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:00:30 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:02:37 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:01:58 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:02:02 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:00:31 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:01:34 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.000 |  |
| 2026-06-11 09:01:43 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.005 |  |
| 2026-06-11 09:00:23 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-06-11 09:05:28 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-06-11 09:02:45 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.021 |  |
| 2026-06-11 09:02:34 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.029 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)