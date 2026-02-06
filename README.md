# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--06_08:05:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **65,433 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 08:05:53 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-06 08:05:51 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 08:05:39 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.142 |  |
| 2026-02-06 08:05:33 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-02-06 08:05:28 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-02-06 08:05:21 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.130 |  |
| 2026-02-06 08:04:30 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 08:04:30 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | -0.078 |  |
| 2026-02-06 08:03:16 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.029 |  |
| 2026-02-06 08:02:57 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-06 08:02:49 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-06 08:02:46 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.023 |  |
| 2026-02-06 08:02:43 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | -0.012 |  |
| 2026-02-06 08:02:29 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.067 |  |
| 2026-02-06 08:02:27 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.040 |  |
| 2026-02-06 08:02:12 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 08:02:10 | Weraganthota (Mahaweli Ganga) | -2.18 | 🟢 Normal | -0.010 |  |
| 2026-02-06 08:01:54 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.025 |  |
| 2026-02-06 08:01:50 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 08:01:50 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-06 08:01:48 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-06 08:01:23 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-06 08:01:02 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-06 07:24:55 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-06 07:20:51 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-02-06 07:14:08 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-06 07:13:07 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-06 07:12:21 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.009 |  |
| 2026-02-06 07:11:02 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | -0.012 |  |
| 2026-02-06 07:10:22 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-06 06:00:27 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-02-06 08:01:02 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-06 06:05:56 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-06 07:06:14 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-02-06 08:01:50 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-06 08:04:30 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 08:01:50 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 07:02:18 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-06 07:02:37 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-06 07:02:50 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-06 08:01:23 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-06 08:02:57 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 07:20:51 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-02-06 08:02:12 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 08:05:51 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 08:05:53 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-06 08:02:49 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:09:32 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-06 07:00:37 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-06 07:24:55 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-06 07:02:49 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-06 07:12:21 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.009 |  |
| 2026-02-06 08:02:10 | Weraganthota (Mahaweli Ganga) | -2.18 | 🟢 Normal | -0.010 |  |
| 2026-02-06 07:03:57 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-06 08:05:33 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-02-06 08:02:43 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | -0.012 |  |
| 2026-02-06 08:05:28 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-02-06 08:02:46 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.023 |  |
| 2026-02-06 08:01:54 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.025 |  |
| 2026-02-06 08:03:16 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.029 |  |
| 2026-02-06 08:02:27 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.040 |  |
| 2026-02-06 08:02:29 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.067 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-06 08:04:30 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | -0.078 |  |
| 2026-02-06 08:05:21 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.130 |  |
| 2026-02-06 08:05:39 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.142 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)