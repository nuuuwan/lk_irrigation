# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--16_08:06:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **74,422 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 08:06:12 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:05:49 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-16 08:05:46 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 08:05:32 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:05:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.057 |  |
| 2026-02-16 08:05:02 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:04:47 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:04:23 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | -0.009 |  |
| 2026-02-16 08:04:01 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.051 |  |
| 2026-02-16 08:03:59 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:03:37 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:03:35 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-16 08:03:31 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:03:01 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.185 |  |
| 2026-02-16 08:02:58 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-02-16 08:02:54 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:02:51 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:02:25 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:02:23 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.099 |  |
| 2026-02-16 08:02:16 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.050 |  |
| 2026-02-16 08:01:51 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-02-16 08:01:48 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | -0.010 |  |
| 2026-02-16 08:01:47 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:01:47 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:01:21 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 08:01:20 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:01:18 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:01:17 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-02-16 08:01:12 | Weraganthota (Mahaweli Ganga) | -2.62 | 🟢 Normal | -0.050 |  |
| 2026-02-16 08:01:08 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.164 |  |
| 2026-02-16 08:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:00:45 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-16 08:00:32 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:00:29 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 1.584 | 🔺 Rising |
| 2026-02-16 07:34:32 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.007 |  |
| 2026-02-16 07:32:30 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-16 07:32:29 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-16 07:30:07 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-02-16 07:27:55 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-16 07:27:54 | Thawalama (Gin Ganga) | 0.24 | 🟢 Normal | 1.584 | 🔺 Rising |
| 2026-02-16 07:23:01 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.008 |  |
| 2026-02-16 07:17:17 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.051 |  |
| 2026-02-16 07:12:09 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.047 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 08:00:29 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 1.584 | 🔺 Rising |
| 2026-02-16 08:01:17 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-02-16 08:05:49 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-16 08:00:45 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-16 08:03:35 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-16 08:01:21 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 08:05:46 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 08:01:47 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:02:25 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:02:54 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:00:32 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:03:31 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:04:47 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-16 07:30:07 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:01:20 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:03:59 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:02:51 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:03:37 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:06:12 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:05:32 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:01:47 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:05:02 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:01:18 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-16 07:34:32 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.007 |  |
| 2026-02-16 07:23:01 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.008 |  |
| 2026-02-16 08:04:23 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | -0.009 |  |
| 2026-02-16 08:01:48 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | -0.010 |  |
| 2026-02-16 08:02:58 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-02-16 08:01:51 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-02-16 07:12:09 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.047 |  |
| 2026-02-16 08:01:12 | Weraganthota (Mahaweli Ganga) | -2.62 | 🟢 Normal | -0.050 |  |
| 2026-02-16 08:02:16 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.050 |  |
| 2026-02-16 08:04:01 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.051 |  |
| 2026-02-16 08:05:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.057 |  |
| 2026-02-16 07:03:20 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.063 |  |
| 2026-02-16 08:02:23 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.099 |  |
| 2026-02-16 08:01:08 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.164 |  |
| 2026-02-16 08:03:01 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.185 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)