# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_09:08:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **194,213 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 09:08:05 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.060 |  |
| 2026-07-01 09:08:04 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:07:29 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.040 |  |
| 2026-07-01 09:07:21 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.009 |  |
| 2026-07-01 09:07:03 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:06:29 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:06:09 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.014 |  |
| 2026-07-01 09:06:04 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:05:56 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:05:42 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.029 |  |
| 2026-07-01 09:05:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.38 | 🟢 Normal | -0.055 |  |
| 2026-07-01 09:04:42 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:04:25 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:04:22 | Hanwella (Kelani Ganga) | 2.05 | 🟢 Normal | -0.051 |  |
| 2026-07-01 09:04:04 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.011 |  |
| 2026-07-01 09:04:00 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.011 |  |
| 2026-07-01 09:03:59 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:03:51 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.039 |  |
| 2026-07-01 09:03:48 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:03:28 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | -0.030 |  |
| 2026-07-01 09:02:55 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.098 |  |
| 2026-07-01 09:02:29 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-07-01 09:02:15 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:01:49 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:01:48 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:01:46 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.040 |  |
| 2026-07-01 09:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 09:01:31 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:01:24 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-07-01 09:01:21 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:01:18 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:00:55 | Nagalagam Street (Kelani Ganga) | 0.03 | 🟢 Normal | -0.064 |  |
| 2026-07-01 09:00:33 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:00:24 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:00:23 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | -0.035 |  |
| 2026-07-01 09:00:06 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 09:01:24 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-07-01 09:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 09:01:21 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:01:31 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:03:48 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:01:18 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:00:06 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:08:04 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:03:59 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:04:25 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-01 08:05:06 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:06:29 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:06:04 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:02:15 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:04:42 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:01:49 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:00:33 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:05:56 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:00:24 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:07:03 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-01 09:07:21 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.009 |  |
| 2026-07-01 09:02:29 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-07-01 09:04:04 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.011 |  |
| 2026-07-01 09:04:00 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.011 |  |
| 2026-07-01 09:06:09 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.014 |  |
| 2026-07-01 07:17:05 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.016 |  |
| 2026-07-01 08:06:47 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | -0.017 |  |
| 2026-07-01 09:05:42 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.029 |  |
| 2026-07-01 09:03:28 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | -0.030 |  |
| 2026-07-01 09:00:23 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | -0.035 |  |
| 2026-07-01 09:03:51 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.039 |  |
| 2026-07-01 09:01:46 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.040 |  |
| 2026-07-01 09:07:29 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.040 |  |
| 2026-07-01 09:04:22 | Hanwella (Kelani Ganga) | 2.05 | 🟢 Normal | -0.051 |  |
| 2026-07-01 09:05:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.38 | 🟢 Normal | -0.055 |  |
| 2026-07-01 09:08:05 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.060 |  |
| 2026-07-01 08:04:01 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | -0.061 |  |
| 2026-07-01 09:00:55 | Nagalagam Street (Kelani Ganga) | 0.03 | 🟢 Normal | -0.064 |  |
| 2026-07-01 09:02:55 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)